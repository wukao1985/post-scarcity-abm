"""Pre-registered analysis for who_keeps_meaning_study (see ../PREREGISTRATION.md).

Usage:  python3 -I analyze.py /path/to/gssr/data  > ../results/output.txt
Needs: pandas numpy statsmodels pyreadr linearmodels
"""
import sys, json
import numpy as np, pandas as pd, pyreadr
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

DATA = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/kjhealy/gssr/data"
RNG = np.random.default_rng(20261116)
NSIM = 2000
OUT = {}

def load(name):
    return list(pyreadr.read_r(f"{DATA}/{name}.rda").values())[0]

def num(s):
    """Numeric codes. Labelled categoricals (panel files) -> 1-based category codes (GSS order);
    numeric-looking categoricals (age, income, ids) -> their numeric value."""
    if isinstance(s.dtype, pd.CategoricalDtype):
        cats = pd.to_numeric(pd.Series(s.cat.categories), errors="coerce")
        if cats.notna().all():
            return pd.to_numeric(s.astype(str), errors="coerce")
        c = s.cat.codes.astype("float64")
        return c.where(c >= 0) + 1
    return pd.to_numeric(s, errors="coerce")

import os
CROSS_CACHE = os.environ.get("CROSS_CACHE")
# ---------------------------------------------------------------- cross-section
g = load("gss_all") if not CROSS_CACHE else None
if CROSS_CACHE:
    OUT = json.load(open(CROSS_CACHE))
else:
    keep = ["year", "age", "wrkstat", "life", "happy", "socfrend", "attend", "marital", "realinc",
            "sex", "race", "degree", "health", "wtssps", "wtssall", "socrel"]
    d = pd.DataFrame({k: num(g[k]) for k in keep})
    d = d[(d.age >= 25) & (d.age <= 64) & d.wrkstat.notna() & (d.wrkstat != 6)].copy()
    d["NW"] = d.wrkstat.isin([4, 5, 7, 8]).astype(float)
    d["w"] = d.wtssps.fillna(d.wtssall)
    d["O1"] = np.where(d.life.notna(), (d.life == 1).astype(float), np.nan)
    d["O2a"] = np.where(d.happy.notna(), (d.happy == 1).astype(float), np.nan)
    d["O2b"] = np.where(d.happy.notna(), (d.happy == 3).astype(float), np.nan)
    d["M1"] = np.where(d.socfrend.notna(), (d.socfrend <= 3).astype(float), np.nan)
    d["M2"] = np.where(d.attend.notna(), (d.attend >= 6).astype(float), np.nan)
    d["M3"] = np.where(d.marital.notna(), (d.marital == 1).astype(float), np.nan)
    d["S4"] = np.where(d.socrel.notna(), (d.socrel <= 3).astype(float), np.nan)
    d["inc_t"] = d.groupby("year").realinc.transform(
        lambda s: pd.qcut(s.rank(method="first"), 3, labels=False) if s.notna().sum() > 30 else np.nan)
    d["agegrp"] = pd.cut(d.age, [24, 39, 54, 64], labels=["25-39", "40-54", "55-64"])

    def design(df, extra, health=True):
        X = pd.DataFrame({"age": df.age, "age2": df.age ** 2 / 100, "female": (df.sex == 2).astype(float)},
                         index=df.index)
        X = X.join(pd.get_dummies(df.race.astype(int), prefix="race", drop_first=True, dtype=float))
        X = X.join(pd.get_dummies(df.degree.astype(int), prefix="deg", drop_first=True, dtype=float))
        if health:
            X = X.join(pd.get_dummies(df.health.astype(int), prefix="hlth", drop_first=True, dtype=float))
        X = X.join(pd.get_dummies(df.year.astype(int), prefix="yr", drop_first=True, dtype=float))
        X = X.loc[:, X.std() > 0]  # drop constant columns (e.g. sex dummy in single-sex subsamples)
        for k, v in extra.items():
            X[k] = v
        return sm.add_constant(X, has_constant="add")

    def fit(df, y, extra_fn, health=True, weighted=True, lpm=False):
        cols = [y, "age", "sex", "race", "degree", "year", "NW", "w"] + (["health"] if health else [])
        sub = df.dropna(subset=cols).copy()
        sub = sub[extra_fn(sub, check=True)].copy()
        X = design(sub, extra_fn(sub), health)
        w = sub.w if weighted else None
        fam = sm.families.Gaussian() if lpm else sm.families.Binomial()
        m = sm.GLM(sub[y], X, family=fam, var_weights=w).fit(cov_type="HC1")
        return m, sub, X

    def ame_nw(m, sub, X, setters, nsim=NSIM, lpm=False):
        """AME of NW (NW=1 vs 0) with other terms re-built by `setters`, via parameter simulation."""
        draws = RNG.multivariate_normal(m.params.values, m.cov_params().values, size=nsim)
        w = sub.w.values / sub.w.values.sum()
        res = {}
        for label, setter in setters.items():
            X1, X0 = setter(X.copy(), 1.0), setter(X.copy(), 0.0)
            def ame(b):
                if lpm:
                    return (X1.values @ b - X0.values @ b) @ w
                p1 = 1 / (1 + np.exp(-(X1.values @ b))); p0 = 1 / (1 + np.exp(-(X0.values @ b)))
                return (p1 - p0) @ w
            res[label] = (ame(m.params.values), np.array([ame(b) for b in draws]))
        return res

    def summ(est, sims):
        se = sims.std()
        lo, hi = np.percentile(sims, [2.5, 97.5])
        from scipy.stats import norm
        p = 2 * (1 - norm.cdf(abs(est / se))) if se > 0 else np.nan
        return {"est": round(float(est), 4), "se": round(float(se), 4), "ci": [round(float(lo), 4), round(float(hi), 4)],
                "p": float(p)}

    def moderator_model(y, M, health=True, weighted=True, lpm=False):
        def extra(sub, check=False):
            if check:
                return sub[M].notna()
            return {"NW": sub.NW, M: sub[M], f"NWx{M}": sub.NW * sub[M]}
        m, sub, X = fit(d, y, extra, health, weighted, lpm)
        def setter(level):
            def s(X, nw):
                X["NW"] = nw; X[M] = level; X[f"NWx{M}"] = nw * level; return X
            return s
        r = ame_nw(m, sub, X, {"M0": setter(0.0), "M1": setter(1.0)}, lpm=lpm)
        diff = r["M1"][1] - r["M0"][1]
        return {"N": int(len(sub)), "penalty_M0": summ(*r["M0"]), "penalty_M1": summ(*r["M1"]),
                "buffer(M1-M0)": summ(r["M1"][0] - r["M0"][0], diff),
                "logit_interaction_p": float(m.pvalues[f"NWx{M}"])}

    def income_model(y, health=True, weighted=True):
        def extra(sub, check=False):
            if check:
                return sub.inc_t.notna()
            e = {"NW": sub.NW}
            for t in (0, 2):
                e[f"inc{t}"] = (sub.inc_t == t).astype(float); e[f"NWxinc{t}"] = sub.NW * e[f"inc{t}"]
            return e
        m, sub, X = fit(d, y, extra, health, weighted)
        def setter(t):
            def s(X, nw):
                X["NW"] = nw
                for k in (0, 2):
                    X[f"inc{k}"] = 1.0 if k == t else 0.0; X[f"NWxinc{k}"] = nw * X[f"inc{k}"]
                return X
            return s
        r = ame_nw(m, sub, X, {"bottom": setter(0), "middle": setter(1), "top": setter(2)})
        sd = np.sqrt(np.average((sub[y] - np.average(sub[y], weights=sub.w)) ** 2, weights=sub.w))
        return {"N": int(len(sub)), "sd_y": float(sd),
                "penalty_bottom": summ(*r["bottom"]), "penalty_middle": summ(*r["middle"]),
                "penalty_top": summ(*r["top"]),
                "top_minus_bottom": summ(r["top"][0] - r["bottom"][0], r["top"][1] - r["bottom"][1]),
                "_sims_tmb_std": (r["top"][1] - r["bottom"][1]) / sd, "_est_tmb_std": (r["top"][0] - r["bottom"][0]) / sd}

    def base_model(y, health=True, weighted=True, lpm=False):
        def extra(sub, check=False):
            return pd.Series(True, index=sub.index) if check else {"NW": sub.NW}
        m, sub, X = fit(d, y, extra, health, weighted, lpm)
        def s(X, nw):
            X["NW"] = nw; return X
        r = ame_nw(m, sub, X, {"all": s}, lpm=lpm)
        return {"N": int(len(sub)), "penalty": summ(*r["all"]), "mean_y_working": float(
            np.average(sub.loc[sub.NW == 0, y], weights=sub.loc[sub.NW == 0, "w"]))}

    def agegroup_model(y):
        def extra(sub, check=False):
            if check:
                return sub.agegrp.notna()
            e = {"NW": sub.NW}
            for a in ("25-39", "55-64"):
                e[f"ag_{a}"] = (sub.agegrp == a).astype(float); e[f"NWxag_{a}"] = sub.NW * e[f"ag_{a}"]
            return e
        m, sub, X = fit(d, y, extra)
        def setter(a):
            def s(X, nw):
                X["NW"] = nw
                for k in ("25-39", "55-64"):
                    X[f"ag_{k}"] = 1.0 if k == a else 0.0; X[f"NWxag_{k}"] = nw * X[f"ag_{k}"]
                return X
            return s
        r = ame_nw(m, sub, X, {a: setter(a) for a in ("25-39", "40-54", "55-64")})
        out = {"N": int(len(sub))}
        for a in r:
            out[f"penalty_{a}"] = summ(*r[a])
        for a in ("25-39", "55-64"):
            out[f"40-54_minus_{a}"] = summ(r["40-54"][0] - r[a][0], r["40-54"][1] - r[a][1])
        return out

    def holm(ps):
        order = sorted(ps, key=lambda k: ps[k]); n = len(ps); out = {}; running = 0
        for i, k in enumerate(order):
            running = max(running, min(1, (n - i) * ps[k])); out[k] = running
        return out

    # ---- confirmatory cross-section
    OUT["H1_O1"] = base_model("O1")
    for h, M in (("H2", "M1"), ("H3", "M2"), ("H4", "M3")):
        OUT[f"{h}_O1"] = moderator_model("O1", M)
    inc_O1 = income_model("O1"); inc_O2b = income_model("O2b")
    OUT["H5a_O1_penalty_top_tercile"] = inc_O1["penalty_top"]
    # H5b: |std(top-bottom) on O2b| > |std(top-bottom) on O1|; approximate the joint by independent sims
    dO2b = np.abs(inc_O2b["_sims_tmb_std"]); dO1 = np.abs(inc_O1["_sims_tmb_std"])
    h5b_diff = dO2b - dO1
    OUT["H5b"] = {"std_buffer_O1": round(float(inc_O1["_est_tmb_std"]), 4),
                  "std_buffer_O2b": round(float(inc_O2b["_est_tmb_std"]), 4),
                  "abs_diff(O2b-O1)": summ(abs(inc_O2b["_est_tmb_std"]) - abs(inc_O1["_est_tmb_std"]), h5b_diff),
                  "p_one_sided_from_sims": float((h5b_diff <= 0).mean())}
    for k in ("_sims_tmb_std", "_est_tmb_std"):
        inc_O1.pop(k); inc_O2b.pop(k)
    OUT["income_model_O1"] = inc_O1; OUT["income_model_O2b"] = inc_O2b
    OUT["H6_O1"] = agegroup_model("O1")
    fam = {"H2": OUT["H2_O1"]["buffer(M1-M0)"]["p"], "H3": OUT["H3_O1"]["buffer(M1-M0)"]["p"],
           "H4": OUT["H4_O1"]["buffer(M1-M0)"]["p"], "H5b": 2 * min(OUT["H5b"]["p_one_sided_from_sims"],
                                                                  1 - OUT["H5b"]["p_one_sided_from_sims"])}
    OUT["Holm_family_H2_H5b"] = holm(fam)

    # ---- robustness / secondary (exploratory)
    R = {}
    R["H1_O1_no_health"] = base_model("O1", health=False)["penalty"]
    R["H1_O1_unweighted"] = base_model("O1", weighted=False)["penalty"]
    R["H1_O1_LPM"] = base_model("O1", lpm=True)["penalty"]
    for M in ("M1", "M2", "M3"):
        R[f"{M}_O1_LPM_buffer"] = moderator_model("O1", M, lpm=True)["buffer(M1-M0)"]
        R[f"{M}_O2a_buffer"] = moderator_model("O2a", M)
        R[f"{M}_O2b_buffer"] = moderator_model("O2b", M)
    R["S4_relatives_O1"] = moderator_model("O1", "S4")
    R["H1_O2a"] = base_model("O2a"); R["H1_O2b"] = base_model("O2b")
    # S1 by non-work type (each type vs working)
    for code, name in ((4, "unemployed"), (5, "retired_lt65"), (7, "keeping_house"), (8, "other")):
        sub_mask = d.wrkstat.isin([1, 2, 3, code])
        dd = d
        d = dd[sub_mask].copy()
        R[f"S1_{name}_O1"] = base_model("O1")["penalty"]
        R[f"S1_{name}_O2b"] = base_model("O2b")["penalty"]
        d = dd
    # S1 by sex
    for sx, name in ((1, "men"), (2, "women")):
        dd = d; d = dd[dd.sex == sx].copy()
        R[f"S1_{name}_O1"] = base_model("O1")["penalty"]; d = dd
    # S2 by decade
    for lo in (1970, 1980, 1990, 2000, 2010, 2020):
        dd = d; d = dd[(dd.year >= lo) & (dd.year < lo + 10)].copy()
        R[f"S2_{lo}s_O1"] = base_model("O1")["penalty"]; d = dd
    OUT["robustness_exploratory"] = R


    json.dump(OUT, open(os.environ.get("CROSS_OUT", "/tmp/cross.json"), "w"), default=float)
# ---------------------------------------------------------------- panels
frames = []
for tag in ("06", "08", "10"):
    p = load(f"gss_panel{tag}_long")
    cols = ["firstid", "wave", "age", "wrkstat", "life", "socfrend", "marital", "health", "realinc"]
    q = pd.DataFrame({k: num(p[k]) for k in cols}); q["panel"] = tag
    q["pid"] = tag + "_" + q.firstid.astype("Int64").astype(str)
    frames.append(q)
P = pd.concat(frames, ignore_index=True)
P = P[P.wrkstat.notna() & P.life.notna() & (P.wrkstat != 6)].copy()
P["NW"] = P.wrkstat.isin([4, 5, 7, 8]).astype(float)
P["O1"] = (P.life == 1).astype(float)
P["married"] = (P.marital == 1).astype(float)
P["loginc"] = np.log(P.realinc.clip(lower=1)).fillna(0); P["inc_miss"] = P.realinc.isna().astype(float)
P["hlth_fair_poor"] = (P.health >= 3).astype(float)
P["age2"] = P.age ** 2 / 100
base = P[(P.wave == 1) & (P.NW == 0) & (P.age >= 25) & (P.age <= 62)]
P = P[P.pid.isin(base.pid)].copy()
P = P.merge(base[["pid", "socfrend"]].rename(columns={"socfrend": "socfrend_w1"}), on="pid", how="left", suffixes=("", "_b"))
P["M1_w1"] = np.where(P.socfrend_w1.notna(), (P.socfrend_w1 <= 3).astype(float), np.nan)
P["pw"] = P.panel + "_" + P.wave.astype(int).astype(str)
for k in sorted(P.pw.unique())[1:]:
    P[f"pw_{k}"] = (P.pw == k).astype(float)
pwcols = [c for c in P.columns if c.startswith("pw_")]
ctrl = ["age2", "married", "hlth_fair_poor", "loginc", "inc_miss"] + pwcols
counts = P.groupby("pid").size(); P = P[P.pid.isin(counts[counts >= 2].index)].copy()
PI = P.set_index(["pid", "wave"])
m7 = PanelOLS(PI.O1, PI[["NW"] + ctrl], entity_effects=True, drop_absorbed=True).fit(cov_type="clustered", cluster_entity=True)
exits = int(P.groupby("pid").NW.max().sum())
OUT["H7_panel"] = {"persons": int(P.pid.nunique()), "obs": int(len(P)), "persons_who_exit": exits,
                   "NW_within": round(float(m7.params["NW"]), 4), "se": round(float(m7.std_errors["NW"]), 4),
                   "p": float(m7.pvalues["NW"])}
P8 = P[P.M1_w1.notna()].copy(); P8["NWxM1"] = P8.NW * P8.M1_w1
PI8 = P8.set_index(["pid", "wave"])
m8 = PanelOLS(PI8.O1, PI8[["NW", "NWxM1"] + ctrl], entity_effects=True, drop_absorbed=True).fit(cov_type="clustered", cluster_entity=True)
OUT["H8_panel"] = {"persons": int(P8.pid.nunique()), "exits": int(P8.groupby("pid").NW.max().sum()),
                   "NW": round(float(m8.params["NW"]), 4), "NWxM1": round(float(m8.params["NWxM1"]), 4),
                   "se_NWxM1": round(float(m8.std_errors["NWxM1"]), 4), "p_NWxM1": float(m8.pvalues["NWxM1"])}
# P1 placebo: working at w1 and w2; does exit at w3 predict O1 change w1->w2?
wide = P.pivot_table(index="pid", columns="wave", values=["NW", "O1"])
wide = wide.dropna(subset=[("NW", 1.0), ("NW", 2.0), ("NW", 3.0), ("O1", 1.0), ("O1", 2.0)])
wide = wide[(wide[("NW", 1.0)] == 0) & (wide[("NW", 2.0)] == 0)]
chg = wide[("O1", 2.0)] - wide[("O1", 1.0)]; later_exit = wide[("NW", 3.0)]
mp = sm.OLS(chg, sm.add_constant(later_exit.rename("exit_w3"))).fit(cov_type="HC1")
OUT["P1_placebo"] = {"n": int(len(chg)), "later_exiters": int(later_exit.sum()),
                     "pre_exit_change_diff": round(float(mp.params["exit_w3"]), 4),
                     "se": round(float(mp.bse["exit_w3"]), 4), "p": float(mp.pvalues["exit_w3"])}

print(json.dumps(OUT, indent=1, ensure_ascii=False, default=float))
