#!/usr/bin/env python3
"""RT-04B step 4 — figures for PAPER.md."""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG  = os.path.join(HERE, "figures"); os.makedirs(FIG, exist_ok=True)
CELLS= os.path.join(HERE, "data_cells.csv")
EXP  = os.path.join(HERE, "exposure_inputs", "occ_exposure.csv")
SHOCK = 202211
AGE = ["18_24","25_54","55_64"]

def ymd(ym): return pd.to_datetime(f"{ym//100}-{ym%100:02d}-01")

def load_q():
    cells = pd.read_csv(CELLS); occ = pd.read_csv(EXP)[["census_code","lm_aioe_z"]]
    df = cells[cells.ageband.isin(AGE) & cells.cow.isin([4,7])].merge(
            occ, left_on="occ", right_on="census_code").dropna(subset=["lm_aioe_z"])
    # employment-weighted exposure quartiles on the pre-period
    pre = df[df.ym < SHOCK]
    w = pre.groupby("occ").emp_wt.sum()
    e = df.drop_duplicates("occ").set_index("occ").lm_aioe_z
    qcut = pd.qcut(e.reindex(w.index), 4, labels=["Q1","Q2","Q3","Q4"])
    df["q"] = df.occ.map(qcut.to_dict())
    return df

def fig1_event(df):
    """Indexed employment in top-exposure quartile, no-contract vs salaried, over time."""
    g = df[df.q=="Q4"].groupby(["ym","cow"]).emp_wt.sum().unstack()
    base = g[g.index < SHOCK].mean()
    idx = g / base * 100
    fig, ax = plt.subplots(figsize=(9,5))
    for cow,lab,c in [(4,"Salaried (private wage/salary)","#1f77b4"),
                      (7,"No-contract (unincorporated self-employed)","#d62728")]:
        ax.plot([ymd(x) for x in idx.index], idx[cow], marker="o", ms=3, label=lab, color=c)
    ax.axvline(ymd(SHOCK), color="k", ls="--", lw=1); ax.text(ymd(SHOCK), ax.get_ylim()[1]*0.98,
              " ChatGPT", va="top", fontsize=8)
    ax.axhline(100, color="grey", lw=.6)
    ax.set_title("Employment in the most AI-exposed occupations (Q4),\nindexed to pre-ChatGPT mean = 100")
    ax.set_ylabel("Employment index (pre-shock = 100)"); ax.legend(fontsize=8); ax.grid(alpha=.25)
    fig.tight_layout(); fig.savefig(f"{FIG}/fig1_q4_employment.png", dpi=130); plt.close()

def fig2_eventstudy():
    p = os.path.join(HERE,"event_study.csv")
    if not os.path.exists(p): return
    es = pd.read_csv(p)
    fig, ax = plt.subplots(figsize=(9,5))
    ax.errorbar(es.approx_month_offset, es.coef, yerr=[es.coef-es.lo, es.hi-es.coef],
                fmt="o-", capsize=3, color="#6a3d9a")
    ax.axhline(0, color="grey", lw=.6); ax.axvline(0, color="k", ls="--", lw=1)
    ax.text(0, ax.get_ylim()[1]*0.96, " ChatGPT", fontsize=8, va="top")
    ax.set_title("Event study: no-contract minus salaried employment response to AI exposure\n"
                 "(triple-interaction coefficient by 6-month block; <0 = contract-buffer)")
    ax.set_xlabel("Months relative to 2022-11"); ax.set_ylabel("β₃ (PPML, per exposure-SD)")
    ax.grid(alpha=.25); fig.tight_layout(); fig.savefig(f"{FIG}/fig2_event_study.png", dpi=130); plt.close()

def fig3_ddd_bars(df):
    """Pre/post % change in employment by exposure quartile and class."""
    g = df.assign(post=(df.ym>=SHOCK).astype(int)).groupby(["q","cow","post"]).emp_wt.mean().unstack("post")
    chg = (g[1]/g[0]-1)*100
    chg = chg.unstack("cow")
    fig, ax = plt.subplots(figsize=(8,5))
    x = np.arange(len(chg)); w=.38
    ax.bar(x-w/2, chg[4], w, label="Salaried", color="#1f77b4")
    ax.bar(x+w/2, chg[7], w, label="No-contract", color="#d62728")
    ax.set_xticks(x); ax.set_xticklabels(chg.index)
    ax.axhline(0,color="grey",lw=.6)
    ax.set_title("Mean employment change (post vs pre ChatGPT) by AI-exposure quartile & class")
    ax.set_ylabel("% change"); ax.set_xlabel("AI-exposure quartile (Q4 = most exposed)")
    ax.legend(); ax.grid(alpha=.25, axis="y"); fig.tight_layout()
    fig.savefig(f"{FIG}/fig3_ddd_bars.png", dpi=130); plt.close()

def main():
    df = load_q()
    fig1_event(df); fig2_eventstudy(); fig3_ddd_bars(df)
    print("figures written to", FIG)

if __name__ == "__main__":
    main()
