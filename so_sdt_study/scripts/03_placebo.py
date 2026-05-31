"""03 — 安慰剂检验：假冲击 2021-11-30。检验 H3 的因果性。
结论：z_rel 在假冲击 OR=0.31，与真冲击 OR=0.28 几乎相同 →
关系型"迁移而非退出"是固有习性，非 ChatGPT 驱动。H3 因果解释被否决。"""
import pandas as pd, numpy as np
import statsmodels.formula.api as smf
RES="../data_collection/results/"
pb=pd.concat([pd.read_csv(f"{RES}placebo_{i}.csv") for i in (1,2,3,4)],ignore_index=True).drop_duplicates("UserId")
def z(s):
    s=s.astype(float); sd=s.std(ddof=0); return (s-s.mean())/(sd if sd>0 else 1)
pb["z_comp"]=z(pb["CompetenceProxy"]); pb["z_stat"]=z(pb["StatusProxy"])
pb["z_rel"]=z((z(pb["RelCommentRatio"])+z(pb["RelEditsOthers"]))/2)
pb["log_pre_ans"]=np.log1p(pb["PreAnsCount"]); pb["log_rep"]=np.log1p(pb["Reputation"]); pb["tenure_years"]=pb["AccountAgeDays"]/365.25
last=pd.to_datetime(pb["LastAnswerAfter"],errors="coerce"); ostart=pd.Timestamp("2022-02-01"); oend=pd.Timestamp("2022-11-30")
total=(oend-ostart).days/30.44
pb["active_months"]=((last-ostart).dt.days/30.44).fillna(0).clip(lower=0)
pb["exit_K6"]=((total-pb["active_months"])>=6).astype(int)
pb["post_engage"]=pb["PostComments"]+pb["PostEdits"]
pb["outcome3"]=np.where(pb["exit_K6"]==0,"active",np.where(pb["post_engage"]>0,"migration","exit"))
sub=pb[pb["outcome3"].isin(["exit","migration"])].copy(); sub["is_exit"]=(sub["outcome3"]=="exit").astype(int)
m=smf.logit("is_exit ~ z_comp+z_stat+z_rel+log_pre_ans+log_rep+tenure_years",data=sub).fit(disp=0)
print(f"placebo cohort {len(pb)}, stoppers {len(sub)}")
print(pd.DataFrame({"OR":np.exp(m.params),"p":m.pvalues}).loc[["z_comp","z_stat","z_rel"]].round(4))
print("\n真冲击 z_rel OR=0.28 vs 安慰剂 OR=0.31 → 几乎相同 → H3因果否决")
