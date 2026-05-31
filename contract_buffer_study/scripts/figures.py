#!/usr/bin/env python3
"""RT-04B step 4 — figures for PAPER.md (faithful to the pre-registered PPML DDD)."""
import os, json, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG  = os.path.join(HERE, "figures"); os.makedirs(FIG, exist_ok=True)
CELLS= os.path.join(HERE, "data_cells.csv.gz")
EXP  = os.path.join(HERE, "exposure_inputs", "occ_exposure.csv")
SHOCK = 202211
AGE = ["18_24","25_54","55_64"]

def ymd(ym): return pd.to_datetime(f"{ym//100}-{ym%100:02d}-01")

def load_q(window=(202107,202604), shock=SHOCK):
    cells = pd.read_csv(CELLS); occ = pd.read_csv(EXP)[["census_code","lm_aioe_z"]]
    df = cells[cells.ageband.isin(AGE) & cells.cow.isin([4,7])].merge(
            occ, left_on="occ", right_on="census_code").dropna(subset=["lm_aioe_z"])
    df = df[(df.ym>=window[0]) & (df.ym<=window[1])]
    pre = df[df.ym < shock]; w = pre.groupby("occ").emp_wt.sum()
    e = df.drop_duplicates("occ").set_index("occ").lm_aioe_z
    qcut = pd.qcut(e.reindex(w.index), 4, labels=["Q1","Q2","Q3","Q4"])
    df["q"] = df.occ.map(qcut.to_dict())
    return df

def fig1_eventstudy():
    """LEAD: the pre-registered dynamic — beta3 by event-time, flat pre-trends, no post descent."""
    p = os.path.join(HERE,"event_study.csv")
    if not os.path.exists(p): return
    es = pd.read_csv(p)
    fig, ax = plt.subplots(figsize=(9,5))
    ax.errorbar(es.approx_month_offset, es.coef*100, yerr=[(es.coef-es.lo)*100,(es.hi-es.coef)*100],
                fmt="o-", capsize=3, color="#6a3d9a", lw=1.5)
    ax.axhline(0, color="grey", lw=.7); ax.axvline(0, color="k", ls="--", lw=1)
    ax.text(0.5, ax.get_ylim()[1]*0.92, "ChatGPT", fontsize=9)
    ax.axvspan(ax.get_xlim()[0], 0, color="grey", alpha=0.06)
    ax.set_title("Contract-buffer effect over time (pre-registered event study)\n"
                 "β₃ = extra employment response of no-contract vs salaried to AI exposure")
    ax.set_xlabel("Months relative to ChatGPT (2022-11)")
    ax.set_ylabel("β₃ per exposure-SD (%)  ·  <0 would support contract buffer")
    ax.grid(alpha=.25); fig.tight_layout(); fig.savefig(f"{FIG}/fig1_event_study.png", dpi=130); plt.close()

def fig2_coefplot():
    """The null is robust: beta3 across specifications, all CIs cross zero; placebo identical."""
    js = json.load(open(os.path.join(HERE,"results_summary.json")))
    rows = [("Primary (LM AIOE)", js["primary"]["beta3"]),
            ("Base AIOE",          js["robustness"]["base AIOE exposure"]),
            ("Age 25–54",          js["robustness"]["age 25-54"]),
            ("Age 16+",            js["robustness"]["age 16+"]),
            ("Cell n≥10",          js["robustness"]["cell n>=10"]),
            ("Cell n≥5",           js["robustness"]["cell n>=5"]),
            ("Early window 22-23", js["early_window"]),
            ("PLACEBO (pre-AI)",   js["placebo"])]
    labels=[r[0] for r in rows]
    coef=np.array([r[1]["coef"]*100 for r in rows])
    lo=np.array([r[1]["lo"]*100 for r in rows]); hi=np.array([r[1]["hi"]*100 for r in rows])
    y=np.arange(len(rows))[::-1]
    fig, ax = plt.subplots(figsize=(8.5,5))
    cols=["#333"]*7+["#c44"]
    ax.errorbar(coef, y, xerr=[coef-lo, hi-coef], fmt="o", capsize=3, color="#333", ecolor="#888")
    ax.scatter(coef[-1:], y[-1:], color="#c44", zorder=5)
    ax.axvline(0, color="grey", lw=.8)
    ax.set_yticks(y); ax.set_yticklabels(labels)
    ax.set_xlabel("β₃: no-contract × exposure × post, per exposure-SD (%)")
    ax.set_title("Contract-buffer coefficient is null across every specification\n"
                 "(negative would support the buffer; all confidence intervals cross zero)")
    ax.grid(alpha=.25, axis="x"); fig.tight_layout()
    fig.savefig(f"{FIG}/fig2_coef_robustness.png", dpi=130); plt.close()

def fig3_descriptive():
    """Honest descriptive: total-employment % change by exposure quartile & class (size-weighted)."""
    df = load_q(); df["post"]=(df.ym>=SHOCK).astype(int)
    nmo = df.groupby("post").ym.nunique()
    avg = df.groupby(["q","cow","post"]).emp_wt.sum().unstack("post").div(nmo, axis=1)
    chg = ((avg[1]/avg[0]-1)*100).unstack("cow")
    fig, ax = plt.subplots(figsize=(8.5,5))
    x=np.arange(len(chg)); w=.38
    ax.bar(x-w/2, chg[4], w, label="Salaried (private wage/salary)", color="#1f77b4")
    ax.bar(x+w/2, chg[7], w, label="No-contract (unincorp. self-employed)", color="#d62728")
    ax.set_xticks(x); ax.set_xticklabels(chg.index); ax.axhline(0,color="grey",lw=.7)
    ax.set_title("Employment change after ChatGPT, by AI-exposure quartile & class\n"
                 "(size-weighted totals; the no-contract drop is broad, not concentrated in exposed occ.)")
    ax.set_ylabel("% change, post vs pre"); ax.set_xlabel("AI-exposure quartile (Q4 = most exposed)")
    ax.legend(fontsize=8); ax.grid(alpha=.25, axis="y"); fig.tight_layout()
    fig.savefig(f"{FIG}/fig3_descriptive.png", dpi=130); plt.close()

def main():
    fig1_eventstudy(); fig2_coefplot(); fig3_descriptive()
    # clean up superseded figures
    for old in ["fig1_q4_employment.png","fig2_event_study.png","fig3_ddd_bars.png"]:
        p=os.path.join(FIG,old)
        if os.path.exists(p): os.remove(p)
    print("figures written:", sorted(os.listdir(FIG)))

if __name__ == "__main__":
    main()
