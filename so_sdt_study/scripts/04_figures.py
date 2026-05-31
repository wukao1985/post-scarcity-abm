"""04 — 生成 PAPER.md 的三张图。"""
import pandas as pd, numpy as np, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE=os.path.dirname(__file__); RES=os.path.join(HERE,"..","data_collection","results")
FIG=os.path.join(HERE,"..","figures"); os.makedirs(FIG,exist_ok=True)
df=pd.read_csv(os.path.join(RES,"analysis_dataset.csv"))
df["rep_band"]=pd.cut(df["Reputation"],[0,500,2000,10000,1e9],labels=["0–500","500–2k","2k–10k","10k+"])
bands=["0–500","500–2k","2k–10k","10k+"]; types=["competence","status","relatedness"]
# Fig1
fig,ax=plt.subplots(figsize=(7,4.5)); x=np.arange(len(bands)); w=0.25
for i,t in enumerate(types):
    ax.bar(x+(i-1)*w,[df[(df.rep_band==b)&(df.dominant_type==t)]["exit_K6"].mean() for b in bands],w,label=t)
ax.set_xticks(x); ax.set_xticklabels(bands); ax.set_xlabel("Reputation band")
ax.set_ylabel("12-month exit rate (K=6)"); ax.set_title("Exit rate by reputation and motivation type\n(reputation dominates; status not highest — H1 rejected)")
ax.legend(title="Dominant type"); plt.tight_layout(); plt.savefig(f"{FIG}/fig1_exit_by_rep_type.png",dpi=130); plt.close()
# Fig2
fig,ax=plt.subplots(figsize=(6,4))
ax.bar(["Real shock\n(Nov 2022)","Placebo\n(Nov 2021)"],[0.28,0.31],color=["#c0392b","#7f8c8d"],width=0.5)
ax.axhline(1.0,ls="--",c="k",lw=0.8,label="OR=1 (no effect)"); ax.set_ylim(0,1.1)
ax.set_ylabel("Relatedness OR (exit vs migration)")
ax.set_title("H3 placebo failure: the migration effect predates ChatGPT\n(0.28 vs 0.31 — essentially identical)")
for i,v in enumerate([0.28,0.31]): ax.text(i,v+0.03,f"OR={v}",ha="center")
ax.legend(); plt.tight_layout(); plt.savefig(f"{FIG}/fig2_placebo.png",dpi=130); plt.close()
# Fig3
fig,ax=plt.subplots(figsize=(6.5,4))
act=[(df[df.dominant_type==t]["outcome3"]=="active").mean() for t in types]
mig=[(df[df.dominant_type==t]["outcome3"]=="migration").mean() for t in types]
ext=[(df[df.dominant_type==t]["outcome3"]=="exit").mean() for t in types]
ax.bar(types,act,label="active",color="#27ae60"); ax.bar(types,mig,bottom=act,label="migration",color="#2980b9")
ax.bar(types,ext,bottom=np.array(act)+np.array(mig),label="exit",color="#c0392b")
ax.set_ylabel("share"); ax.set_title("Post-shock outcome composition by motivation type")
ax.legend(); plt.tight_layout(); plt.savefig(f"{FIG}/fig3_outcome_composition.png",dpi=130); plt.close()
print("figures written to", FIG)
