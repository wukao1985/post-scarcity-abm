#!/usr/bin/env python3
"""
RT-04B step 3 — frozen analysis (DESIGN.md §7).

Primary: PPML triple-difference of weighted employment count in
occupation x class x month cells:

   E[o,c,t] ~ PPML( occ#class FE + month FE
                    + b1 Post*Exp + b2 Post*NoContract + b3 Post*Exp*NoContract )

b3 (Post x Exp x NoContract) is THE contract-buffer coefficient:
   b3 < 0  -> contract-buffer mechanism (the book's hinge)
   b3 = 0  -> pure-substitutability rival (Post*Exp < 0, common to both classes)

Plus: event-study dynamics (H1b earlier), incorporated-SE gradient (H2),
placebo shock (2022-05), base-AIOE robustness, age bands, cell thresholds.
Writes RESULTS.md and a machine-readable results_summary.json.
"""
import os, json, warnings
import numpy as np, pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
warnings.simplefilter("ignore")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CELLS = os.path.join(HERE, "data_cells.csv")
EXP   = os.path.join(HERE, "exposure_inputs", "occ_exposure.csv")
SHOCK = 202211
PLACEBO = 202205
PRIMARY_AGE = ["18_24","25_54","55_64"]
SALARIED, INC_SE, UNINC_SE = 4, 6, 7

def load(age_bands=PRIMARY_AGE, classes=(SALARIED, UNINC_SE), exposure="lm_aioe_z",
         min_n=0, window=None, balance=True):
    cells = pd.read_csv(CELLS)
    occ = pd.read_csv(EXP)[["census_code", exposure]].rename(columns={exposure:"exp"})
    df = cells[cells.ageband.isin(age_bands) & cells.cow.isin(classes)].copy()
    df = df.merge(occ, left_on="occ", right_on="census_code", how="inner").dropna(subset=["exp"])
    # collapse over age bands -> occ x class x month
    g = df.groupby(["occ","cow","ym","exp"], as_index=False).agg(
            emp_wt=("emp_wt","sum"), n_raw=("n_raw","sum"), hours_wt=("hours_wt","sum"))
    if window:
        g = g[(g.ym >= window[0]) & (g.ym <= window[1])]
    if balance:
        # PPML wants months where an established cell's employment is 0 to enter as 0,
        # not vanish. Balance over (occ,cow) that appear in the pre-shock portion of the
        # window, across all months in window.
        first = g.ym.min()
        cutoff = SHOCK if (not window or window[0] < SHOCK) else first + 1
        established = g[g.ym < cutoff][["occ","cow"]].drop_duplicates()
        cells_set = g[["occ","cow","exp"]].drop_duplicates().merge(established, on=["occ","cow"])
        allmonths = sorted(g.ym.unique())
        full = (cells_set.assign(key=1).merge(pd.DataFrame({"ym":allmonths,"key":1}), on="key")
                         .drop(columns="key"))
        g = full.merge(g.drop(columns="exp"), on=["occ","cow","ym"], how="left")
        for c in ["emp_wt","n_raw","hours_wt"]:
            g[c] = g[c].fillna(0.0)
    if min_n:   # drop thin cells (per-month respondent floor)
        g = g[g.n_raw >= min_n]
    return g

def fit_ddd(g, shock, value="emp_wt", nocontract_class=UNINC_SE):
    d = g.copy()
    d["post"] = (d.ym >= shock).astype(int)
    d["nocon"] = (d.cow == nocontract_class).astype(int)
    d["cell"] = d.occ.astype(str)+"_"+d.cow.astype(str)
    d["ymf"]  = d.ym.astype(str)
    d["y"] = d[value]
    # PPML via GLM Poisson; FE as categoricals; cluster by occupation
    m = smf.glm("y ~ post:exp + post:nocon + post:exp:nocon + C(cell) + C(ymf)",
                data=d, family=sm.families.Poisson())
    res = m.fit(cov_type="cluster", cov_kwds={"groups": d.occ})
    return res, d

def grab(res, name):
    for p in res.params.index:
        if p.replace(" ","") == name.replace(" ",""):
            ci = res.conf_int().loc[p]
            return dict(coef=float(res.params[p]), se=float(res.bse[p]),
                        z=float(res.tvalues[p]), p=float(res.pvalues[p]),
                        lo=float(ci[0]), hi=float(ci[1]))
    return None

def pct(b):  # PPML coef -> approx % effect
    return (np.exp(b)-1)*100

def event_study(g, shock, value="emp_wt"):
    d = g.copy()
    d["nocon"] = (d.cow == UNINC_SE).astype(int)
    d["cell"]  = d.occ.astype(str)+"_"+d.cow.astype(str)
    d["ymf"]   = d.ym.astype(str)
    d["y"]     = d[value]
    d["post"]  = (d.ym >= shock).astype(int)
    # months since shock, bucketed into 6-month blocks; base block = -1 (the 6 mo before shock)
    d["blk"] = (((d.ym//100 - shock//100)*12 + (d.ym%100 - shock%100)) // 6).astype(int)
    base = -1
    blocks = [b for b in sorted(d.blk.unique()) if b != base]
    # explicit numeric interaction columns, one per block
    cols = []
    for b in blocks:
        c = f"b_{b}".replace("-","m")
        d[c] = (d.blk == b).astype(int) * d.nocon * d.exp
        cols.append((b, c))
    d["post_exp"]   = d.post * d.exp
    d["post_nocon"] = d.post * d.nocon
    rhs = " + ".join([c for _,c in cols]) + " + post_exp + post_nocon + C(cell) + C(ymf)"
    res = smf.glm(f"y ~ {rhs}", data=d, family=sm.families.Poisson()).fit(
                  cov_type="cluster", cov_kwds={"groups": d.occ})
    rows = []
    for b, c in cols:
        gg = grab(res, c)
        if gg: rows.append((b, b*6, gg["coef"], gg["lo"], gg["hi"], gg["p"]))
    return pd.DataFrame(rows, columns=["block","approx_month_offset","coef","lo","hi","p"])

def main():
    out = {}
    print("="*70); print("RT-04B PRIMARY: PPML triple-difference (contract buffer)"); print("="*70)
    g = load()
    res, d = fit_ddd(g, SHOCK)
    b3 = grab(res, "post:exp:nocon"); b1 = grab(res, "post:exp"); b2 = grab(res, "post:nocon")
    out["primary"] = dict(beta3=b3, beta1_postExp=b1, beta2_postNoContract=b2,
                          n_cells=int(d.cell.nunique()), n_obs=int(len(d)),
                          n_occ=int(d.occ.nunique()), months=sorted(int(x) for x in d.ym.unique()))
    print(f"\nN: {len(d)} obs, {d.cell.nunique()} cells, {d.occ.nunique()} occupations, "
          f"{d.ym.nunique()} months ({min(d.ym)}-{max(d.ym)})")
    print(f"\nbeta3  Post x Exp x NoContract = {b3['coef']:+.4f}  (SE {b3['se']:.4f}, p={b3['p']:.4g})  "
          f"~ {pct(b3['coef']):+.1f}% per exposure-SD")
    print(f"       95% CI [{b3['lo']:+.4f}, {b3['hi']:+.4f}]  -> "
          f"[{pct(b3['lo']):+.1f}%, {pct(b3['hi']):+.1f}%]")
    print(f"beta1  Post x Exp (common)      = {b1['coef']:+.4f}  (p={b1['p']:.4g})  ~ {pct(b1['coef']):+.1f}%")
    print(f"beta2  Post x NoContract        = {b2['coef']:+.4f}  (p={b2['p']:.4g})")
    verdict = ("CONTRACT-BUFFER supported (beta3<0, sig)" if (b3["hi"]<0)
               else "PURE-SUBSTITUTABILITY favoured (beta3 not<0)" if (b3["lo"]<0<b3["hi"] or b3["lo"]>0)
               else "ambiguous")
    print(f"\nVERDICT (primary): {verdict}")
    out["primary"]["verdict"] = verdict

    # ---- H1b early window ----
    print("\n" + "-"*70); print("H1b EARLIER: beta3 in early post window (2022-11..2023-12)")
    g_e = load(window=(202107, 202312))
    res_e,_ = fit_ddd(g_e, SHOCK); b3e = grab(res_e, "post:exp:nocon")
    out["early_window"] = b3e
    print(f"  beta3(early) = {b3e['coef']:+.4f} (p={b3e['p']:.4g}) ~ {pct(b3e['coef']):+.1f}%")

    # ---- H2 gradient: incorporated SE as middle rung ----
    print("\n" + "-"*70); print("H2 GRADIENT: unincorp(7) vs incorp(6) vs salaried(4)")
    for cls,label in [(UNINC_SE,"unincorp SE (no buffer)"), (INC_SE,"incorp SE (mid)")]:
        gg = load(classes=(SALARIED, cls))
        rr,_ = fit_ddd(gg, SHOCK, nocontract_class=cls)
        bb = grab(rr, "post:exp:nocon")
        out.setdefault("gradient",{})[label] = bb
        print(f"  {label:26s} beta3 vs salaried = {bb['coef']:+.4f} (p={bb['p']:.4g}) ~ {pct(bb['coef']):+.1f}%")

    # ---- Placebo ----
    print("\n" + "-"*70); print("PLACEBO shock 2022-05 (AI-clean window 2021-07..2022-10); expect beta3~0")
    g_p = load(window=(202107, 202210))
    res_p,_ = fit_ddd(g_p, PLACEBO); b3p = grab(res_p, "post:exp:nocon")
    out["placebo"] = b3p
    print(f"  beta3(placebo) = {b3p['coef']:+.4f} (p={b3p['p']:.4g}) ~ {pct(b3p['coef']):+.1f}%")
    out["placebo"]["identification"] = "PASS (placebo null)" if b3p["p"]>0.05 or b3p["lo"]<0<b3p["hi"] else \
                                       "FAIL (placebo significant -> identification suspect)"
    print(f"  identification: {out['placebo']['identification']}")

    # ---- Robustness: base AIOE, age bands, cell thresholds ----
    print("\n" + "-"*70); print("ROBUSTNESS (beta3, primary window)")
    rob = {}
    specs = [("base AIOE exposure", dict(exposure="aioe_z")),
             ("age 25-54",          dict(age_bands=["25_54"])),
             ("age 16+",            dict(age_bands=["16_17","18_24","25_54","55_64","65p"])),
             ("cell n>=10",         dict(min_n=10)),
             ("cell n>=5",          dict(min_n=5)),
             ("hours outcome",      dict())]
    for label, kw in specs:
        val = "hours_wt" if label=="hours outcome" else "emp_wt"
        gg = load(**kw); rr,_ = fit_ddd(gg, SHOCK, value=val); bb = grab(rr, "post:exp:nocon")
        rob[label] = bb
        print(f"  {label:22s} beta3 = {bb['coef']:+.4f} (p={bb['p']:.4g}) ~ {pct(bb['coef']):+.1f}%")
    out["robustness"] = rob

    # ---- Event study ----
    print("\n" + "-"*70); print("EVENT STUDY (beta3 by 6-month block; block -1 = base)")
    try:
        es = event_study(load(), SHOCK)
        out["event_study"] = es.to_dict(orient="records")
        print(es.round(4).to_string(index=False))
        es.to_csv(os.path.join(HERE,"event_study.csv"), index=False)
    except Exception as e:
        print("  event study failed:", e)

    with open(os.path.join(HERE,"results_summary.json"),"w") as f:
        json.dump(out, f, indent=2)
    print("\nwrote results_summary.json")

if __name__ == "__main__":
    main()
