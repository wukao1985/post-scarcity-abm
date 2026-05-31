#!/usr/bin/env python3
"""
RT-04B step 1 — build the occupation-level AI-exposure table (FROZEN design §5).

Bridges CPS detailed occupation (PEIO1OCD, 2018 census occ code) to the AIOE
generative-AI exposure scores (keyed to 2010 SOC) via the Census
"2010 to 2018 Crosswalk" sheet:

    PEIO1OCD (2018 census occ) --> 2010 SOC --> Language-Modeling AIOE  [primary]
                                            --> base AIOE               [robustness]

Mapping rules (frozen):
  - For each 2018 census code, collect the adjacent 2010 SOC codes from the
    crosswalk (the row's own + forward/backward fill, to span split & combine rows).
  - Exposure = mean AIOE over those 2010 SOC codes that exist in AIOE.
  - Broad-SOC fallback: a mapped 2010 SOC absent from AIOE (e.g. 15-1150) is
    expanded to all AIOE SOC codes sharing its non-zero stem (15-115x), averaged.
  - Unmatched census codes (residual "all other" / military) get no exposure and
    are dropped from exposure-based estimation.

Writes the small, committed table: exposure_inputs/occ_exposure.csv
"""
import pandas as pd, numpy as np, re, os
from collections import defaultdict

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXP  = os.path.join(HERE, "exposure_inputs")

def ci(x):
    if pd.isna(x): return np.nan
    s = re.sub(r"\.0$", "", str(x).strip())
    return int(s) if re.fullmatch(r"\d+", s) else np.nan

def soc_ok(x):
    if pd.isna(x): return np.nan
    s = str(x).strip()
    return s if re.match(r"\d\d-\d{4}$", s) else np.nan

def main():
    # --- AIOE scores (2010 SOC) ---
    lm   = pd.read_excel(f"{EXP}/aioe/LM_AIOE_and_AIIE.xlsx", sheet_name="LM AIOE")
    lm.columns = ["soc", "title", "lm"]
    base = pd.read_excel(f"{EXP}/aioe/AIOE_DataAppendix.xlsx", sheet_name="Appendix A")
    base.columns = ["soc", "title", "aioe"]
    lm["soc"] = lm.soc.str.strip(); base["soc"] = base.soc.str.strip()
    lm_map   = dict(zip(lm.soc, lm.lm))
    base_map = dict(zip(base.soc, base.aioe))
    lm_socs   = list(lm.soc)
    base_socs = list(base.soc)

    def score(socset, table, all_socs):
        vals = []
        for s in socset:
            if s in table:
                vals.append(table[s])
            else:                                   # broad-SOC fallback
                stem = s.rstrip("0")
                if len(stem) >= 4:
                    vals += [table[a] for a in all_socs if a.startswith(stem)]
        return np.mean(vals) if vals else np.nan

    # --- Census 2010<->2018 crosswalk ---
    xw = pd.read_excel(f"{EXP}/census2018_occ_soc_crosswalk.xlsx",
                       sheet_name="2010 to 2018 Crosswalk ", header=3, dtype=str)
    xw.columns = ["soc2010", "cen2010", "title2010", "soc2018", "cen2018", "title2018"]
    xw["c2018"] = xw.cen2018.map(ci)
    xw["s2010"] = xw.soc2010.map(soc_ok)
    ff = xw.s2010.ffill(); bf = xw.s2010.bfill()

    m = defaultdict(set)
    for i, row in xw.reset_index(drop=True).iterrows():
        c = row.c2018
        if pd.isna(c): continue
        for src in (row.s2010, ff.iloc[i], bf.iloc[i]):
            if isinstance(src, str):
                m[int(c)].add(src)

    rows = [(c, ";".join(sorted(s)),
             score(s, lm_map, lm_socs), score(s, base_map, base_socs))
            for c, s in m.items()]
    occ = pd.DataFrame(rows, columns=["census_code", "soc2010_set", "lm_aioe", "aioe"])
    occ["lm_aioe"] = pd.to_numeric(occ.lm_aioe)
    occ["aioe"]    = pd.to_numeric(occ.aioe)

    # titles for readability
    titles = pd.read_excel(f"{EXP}/census2018_occ_soc_crosswalk.xlsx",
                           sheet_name="Summary of 2018 Changes", header=2)
    titles.columns = [c.strip() for c in titles.columns]
    tt = titles.assign(c=titles["2018 Census Code"].map(ci)).dropna(subset=["c"])
    occ["title"] = occ.census_code.map(dict(zip(tt.c.astype(int), tt["2018 Census Title"])))

    # z-score the (matched) exposure across occupation codes — FROZEN: unweighted
    for col in ["lm_aioe", "aioe"]:
        z = (occ[col] - occ[col].mean()) / occ[col].std()
        occ[col + "_z"] = z

    occ = occ.sort_values("census_code")
    out = os.path.join(EXP, "occ_exposure.csv")
    occ.to_csv(out, index=False)
    n_match = occ.lm_aioe.notna().sum()
    print(f"wrote {out}: {len(occ)} census codes, LM matched {n_match} ({n_match/len(occ):.0%})")
    print(occ.lm_aioe.describe().round(3).to_string())

if __name__ == "__main__":
    main()
