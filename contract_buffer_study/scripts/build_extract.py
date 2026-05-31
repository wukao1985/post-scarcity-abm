#!/usr/bin/env python3
"""
RT-04B step 2 — build the slim cell-level CPS analysis file (FROZEN design §4, §6, §11).

Source plan (each source spans one internally-consistent layout era):
  2021-07 .. 2023-11 : NBER pre-converted Stata   data.nber.org/cps-basic2/dta/cpsbYYYYMM.dta
  2023-12 .. latest  : Census public-use fixed-width  www2.census.gov/.../basic/mmmYYpub.zip
Cross-source seam (2023-11 NBER vs Census) is validated: weighted class-of-worker
counts must agree. Raw monthly microdata are downloaded to a gitignored cache and
NEVER committed; only the collapsed cell file is committed.

Output (committed, slim):  data_cells.csv  with one row per
  (ym, census_occ_code, class_of_worker, age_band) and columns:
    n_raw     : unweighted # employed persons in the cell
    emp_wt    : sum of final weight (PWCMPWGT/1e4) over employed persons  [employment level]
    hours_wt  : sum of weight*usual-hours over employed-at-work w/ valid hours [hours outcome]
employed := PEMLR in {1,2}; classes kept = {1,2,3,4,5,6,7} (without-pay 8 dropped).
"""
import os, io, sys, zipfile, urllib.request, calendar
import pandas as pd, numpy as np, pyreadstat

HERE  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.environ.get("CPS_CACHE", "/tmp/cps_raw"); os.makedirs(CACHE, exist_ok=True)
OUT   = os.path.join(HERE, "data_cells.csv.gz")

NBER_LAST = (2023, 11)          # NBER cps-basic2 coverage end
START     = (2021, 7)           # frozen primary window start
# END is auto-detected (latest Census month available)

# Census 2023+ fixed-width positions (1-indexed inclusive), from the 2024 record layout
CEN = dict(hrmonth=(16,17), hryear4=(18,21), prtage=(122,123), pemlr=(180,181),
           pehrusl1=(218,219), peio1cow=(432,433), pwcmpwgt=(846,855), peio1ocd=(860,863))
MON = {1:"jan",2:"feb",3:"mar",4:"apr",5:"may",6:"jun",7:"jul",8:"aug",9:"sep",10:"oct",11:"nov",12:"dec"}

def months(start, end):
    y,m = start
    while (y,m) <= end:
        yield y,m
        m += 1
        if m == 13: y,m = y+1,1

def _fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return dest
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 (research; CPS)"} )
    with urllib.request.urlopen(req, timeout=300) as r, open(dest,"wb") as f:
        f.write(r.read())
    return dest

def read_nber(y, m):
    url = f"https://data.nber.org/cps-basic2/dta/cpsb{y}{m:02d}.dta"
    dest = _fetch(url, f"{CACHE}/cpsb{y}{m:02d}.dta")
    # occupation var: peio1ocd pre-2023, ptio1ocd from 2023 redesign
    _, meta = pyreadstat.read_dta(dest, metadataonly=True)
    occvar = "peio1ocd" if "peio1ocd" in meta.column_names else "ptio1ocd"
    cols = ["pemlr","peio1cow",occvar,"prtage","pehrusl1","pwcmpwgt"]
    df,_ = pyreadstat.read_dta(dest, usecols=cols)
    return df.rename(columns={occvar:"occ"})

def read_census(y, m):
    url = f"https://www2.census.gov/programs-surveys/cps/datasets/{y}/basic/{MON[m]}{y%100:02d}pub.zip"
    dest = _fetch(url, f"{CACHE}/{MON[m]}{y%100:02d}pub.zip")
    with zipfile.ZipFile(dest) as z:
        name = [n for n in z.namelist() if n.lower().endswith(".dat") or "pub" in n.lower()][0]
        raw = z.read(name).decode("latin-1").splitlines()
    def col(rec, a, b): return rec[a-1:b]
    rows = []
    for rec in raw:
        if len(rec) < 863: continue
        try:
            rows.append((int(col(rec,*CEN["pemlr"])), int(col(rec,*CEN["peio1cow"])),
                         int(col(rec,*CEN["peio1ocd"])), int(col(rec,*CEN["prtage"])),
                         int(col(rec,*CEN["pehrusl1"])), int(col(rec,*CEN["pwcmpwgt"]))))
        except ValueError:
            continue
    df = pd.DataFrame(rows, columns=["pemlr","peio1cow","occ","prtage","pehrusl1","pwcmpwgt"])
    return df

def age_band(a):
    if   a < 16: return None
    elif a < 18: return "16_17"
    elif a < 25: return "18_24"
    elif a < 55: return "25_54"
    elif a < 65: return "55_64"
    else:        return "65p"

def collapse(df, ym):
    df = df.copy()
    df["w"] = df.pwcmpwgt / 1e4
    emp = df[(df.pemlr.isin([1,2])) & (df.peio1cow.between(1,7)) & (df.occ > 0) & (df.w > 0)].copy()
    emp["ageband"] = emp.prtage.map(age_band)
    emp = emp.dropna(subset=["ageband"])
    # hours: valid usual hours on main job (>=1) among those at work
    emp["hw"] = np.where(emp.pehrusl1.between(1,99), emp.w * emp.pehrusl1, 0.0)
    g = emp.groupby(["occ","peio1cow","ageband"], observed=True).agg(
            n_raw=("w","size"), emp_wt=("w","sum"), hours_wt=("hw","sum")).reset_index()
    g.insert(0, "ym", ym)
    return g.rename(columns={"peio1cow":"cow"})

def latest_census_month():
    """auto-detect newest available Census basic month (probe back from today+1)."""
    import datetime
    d = datetime.date.today()
    for _ in range(6):
        url = f"https://www2.census.gov/programs-surveys/cps/datasets/{d.year}/basic/{MON[d.month]}{d.year%100:02d}pub.zip"
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent":"Mozilla/5.0"})
            if urllib.request.urlopen(req, timeout=30).status == 200:
                return (d.year, d.month)
        except Exception:
            pass
        d = (d.replace(day=1) - datetime.timedelta(days=1)).replace(day=1)
    return NBER_LAST

def validate_seam():
    """NBER vs Census must agree on weighted class-of-worker counts (2023-11)."""
    y,m = 2023,11
    a = collapse(read_nber(y,m), 0).groupby("cow").emp_wt.sum()
    b = collapse(read_census(y,m), 0).groupby("cow").emp_wt.sum()
    cmp = pd.DataFrame({"nber":a,"census":b})
    cmp["pct_diff"] = (cmp.census/cmp.nber - 1)*100
    print("=== seam validation 2023-11 (weighted employment by class of worker) ===")
    print(cmp.round(2).to_string())
    ok = cmp.pct_diff.abs().max() < 2.0
    print("VALIDATION", "PASS" if ok else "FAIL", f"(max |pct diff| = {cmp.pct_diff.abs().max():.2f}%)")
    return ok

def main():
    if "--validate" in sys.argv:
        validate_seam(); return
    end = latest_census_month()
    print(f"window {START} .. {end}")
    parts = []
    for y,m in months(START, end):
        ym = y*100+m
        try:
            df = read_nber(y,m) if (y,m) <= NBER_LAST else read_census(y,m)
            c = collapse(df, ym)
            parts.append(c)
            print(f"  {ym}: {len(df):>7} persons -> {len(c):>5} cells | "
                  f"emp(18-64) {c[c.ageband.isin(['18_24','25_54','55_64'])].emp_wt.sum()/1e6:6.1f}M")
        except Exception as e:
            print(f"  {ym}: SKIP ({type(e).__name__}: {e})")
    cells = pd.concat(parts, ignore_index=True)
    cells.to_csv(OUT, index=False)
    print(f"\nwrote {OUT}: {len(cells)} rows, {cells.ym.nunique()} months, "
          f"{os.path.getsize(OUT)/1e6:.1f} MB")

if __name__ == "__main__":
    main()
