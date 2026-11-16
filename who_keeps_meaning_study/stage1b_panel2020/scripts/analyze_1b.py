"""Stage 1b: held-out test on the GSS 2016-2020 panel (see ../PREREGISTRATION.md, frozen bb3463a)."""
import json, sys
import numpy as np, pandas as pd, pyreadr
import statsmodels.api as sm

SRC = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/kjhealy/gssr/data/gss_panel20.rda"
OUT = sys.argv[2] if len(sys.argv) > 2 else "results/output_1b.json"
SEED = 20261116

raw = pyreadr.read_r(SRC)["gss_panel20"]

def num(s):
    if isinstance(s.dtype, pd.CategoricalDtype):
        cats = pd.to_numeric(pd.Series(s.cat.categories), errors="coerce")
        if cats.notna().all():
            return pd.to_numeric(s.astype(str), errors="coerce")
        c = s.cat.codes.astype("float64"); return c.where(c >= 0) + 1
    return pd.to_numeric(s, errors="coerce")

is16 = num(raw["samptype"]) == 2016
def base(v):
    return pd.Series(np.where(is16, num(raw[f"{v}_1a"]), num(raw[f"{v}_1b"])), index=raw.index)
def fu(v):
    return num(raw[f"{v}_2"])

d = pd.DataFrame({
    "cohort18": (~is16).astype(float),
    "wb": base("wrkstat"), "wf": fu("wrkstat"),
    "age": base("age"), "sex": base("sex"), "race": base("race"), "degree": base("degree"),
    "health": base("health"), "marital": base("marital"), "attend": base("attend"),
    "happy0": base("happy"), "happy1": fu("happy"), "life0": base("life"), "life1": fu("life"),
    "w2": fu("wtssnr") if "wtssnr_2" in raw else fu("wtssall"),
})
d["w2"] = d["w2"].fillna(fu("wtssall"))
d = d[d.wb.isin([1, 2, 3]) & d.wf.notna() & d.age.between(25, 60)].copy()
d["U"] = (d.wf == 4).astype(float)
d["NW"] = d.wf.isin([4, 5, 7, 8]).astype(float)
d["ntt0"] = (d.happy0 == 3).astype(float).where(d.happy0.notna())
d["ntt1"] = (d.happy1 == 3).astype(float).where(d.happy1.notna())
d["nex0"] = (d.life0 != 1).astype(float).where(d.life0.notna())
d["nex1"] = (d.life1 != 1).astype(float).where(d.life1.notna())
d["married"] = (d.marital == 1).astype(float).where(d.marital.notna())
d["weekly"] = (d.attend >= 6).astype(float).where(d.attend.notna())

def X(df, extra):
    x = pd.DataFrame({"age": df.age, "age2": df.age**2 / 100, "female": (df.sex == 2).astype(float),
                      "black": (df.race == 2).astype(float), "orace": (df.race == 3).astype(float),
                      "health": df.health, "cohort18": df.cohort18}, index=df.index)
    x = x.join(pd.get_dummies(df.degree, prefix="deg", drop_first=True).astype(float))
    for e in extra: x[e] = df[e]
    x = x.loc[:, x.std() > 0]
    return sm.add_constant(x)

def fd(df, y0, y1, expo, extra=(), weights=None):
    s = df.dropna(subset=[y0, y1, "age", "sex", "race", "degree", "health", *extra]).copy()
    dy = s[y1] - s[y0]
    x = X(s, [expo, *extra])
    if weights is not None:
        w = s[weights].fillna(s[weights].mean())
        m = sm.WLS(dy, x, weights=w).fit(cov_type="HC1")
    else:
        m = sm.OLS(dy, x).fit(cov_type="HC1")
    return m, s

def summ(m, term, n_exp):
    b, se, p = m.params[term], m.bse[term], m.pvalues[term]
    ci = m.conf_int().loc[term].tolist()
    return {"est": round(b, 4), "se": round(se, 4), "ci": [round(c, 4) for c in ci], "p": float(p), "N": int(m.nobs), "n_exposed": int(n_exp)}

res = {"frozen_plan_commit": "bb3463a", "source_sha256": "8c1d59cc0a7760b2882b78048fcc0a1e22ea9457236847361d06cfab33151252"}
prim = d[d.wf.isin([1, 2, 3, 4])].copy()

m, s = fd(prim, "ntt0", "ntt1", "U"); res["H1b_O2b"] = summ(m, "U", s.U.sum())
m, s = fd(prim, "ntt0", "ntt1", "U", weights="w2"); res["H1b_O2b_weighted"] = summ(m, "U", s.U.sum())

for mod, key in (("married", "H2b"), ("weekly", "H3b")):
    p2 = prim.dropna(subset=[mod]).copy(); p2["UxM"] = p2.U * p2[mod]
    m, s = fd(p2, "ntt0", "ntt1", "U", extra=[mod, "UxM"])
    res[key] = summ(m, "UxM", s.UxM.sum())
    res[key]["U_main_(mod=0)"] = summ(m, "U", s.U.sum())

# H4b: distress vs engagement, independent bootstrap of the difference
rng = np.random.default_rng(SEED)
m_d, s_d = fd(prim, "ntt0", "ntt1", "U"); m_e, s_e = fd(prim, "nex0", "nex1", "U")
res["O1_not_exciting_U"] = summ(m_e, "U", s_e.U.sum())
diffs = []
for _ in range(2000):
    a = s_d.sample(len(s_d), replace=True, random_state=int(rng.integers(1e9))).reset_index(drop=True)
    b = s_e.sample(len(s_e), replace=True, random_state=int(rng.integers(1e9))).reset_index(drop=True)
    try:
        diffs.append(fd(a, "ntt0", "ntt1", "U")[0].params["U"] - fd(b, "nex0", "nex1", "U")[0].params["U"])
    except Exception as e:
        if not diffs and _ == 0: print("bootstrap error:", repr(e)[:300])
diffs = np.array(diffs)
obs = m_d.params["U"] - m_e.params["U"]
res["H4b"] = {"diff": round(float(obs), 4), "ci": [round(float(np.percentile(diffs, 2.5)), 4), round(float(np.percentile(diffs, 97.5)), 4)],
              "p_two_sided": float(min(1, 2 * min((diffs <= 0).mean(), (diffs >= 0).mean()))), "draws": int(len(diffs))}

nw = d[d.wf.isin([1, 2, 3, 4, 5, 7, 8])].copy()
m, s = fd(nw, "ntt0", "ntt1", "NW"); res["H5b"] = summ(m, "NW", s.NW.sum())

# P1b: baseline level among future-unemployed
s = prim.dropna(subset=["ntt0", "age", "sex", "race", "degree", "health"])
m = sm.OLS(s.ntt0, X(s, ["U"])).fit(cov_type="HC1"); res["P1b_baseline_gap"] = summ(m, "U", s.U.sum())

# Holm across H2b-H5b
fam = {"H2b": res["H2b"]["p"], "H3b": res["H3b"]["p"], "H4b": res["H4b"]["p_two_sided"], "H5b": res["H5b"]["p"]}
order = sorted(fam, key=fam.get); k = len(order); run = 0
for i, h in enumerate(order):
    run = max(run, min(1, (k - i) * fam[h])); res.setdefault("holm", {})[h] = run

# descriptive: retirees, raw rates
desc = {}
for lab, cond in (("still_working", d.wf.isin([1, 2, 3])), ("unemployed", d.wf == 4), ("retired", d.wf == 5), ("keeping_house", d.wf == 7)):
    g = d[cond]
    desc[lab] = {"n": int(len(g)), "ntt_base": round(float(g.ntt0.mean()), 3), "ntt_2020": round(float(g.ntt1.mean()), 3)}
res["descriptive"] = desc
json.dump(res, open(OUT, "w"), indent=1, default=float)
print(json.dumps(res, indent=1, default=float))
