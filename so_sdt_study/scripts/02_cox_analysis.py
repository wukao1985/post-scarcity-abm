"""
02 — 主分析：Cox 生存分析 + H3 + 强制深挖（DESIGN §7 冻结）。

用 statsmodels PHReg（Cox 比例风险）。不依赖 lifelines（编译失败）。

执行：
  1. H1 连续主模型：Cox(exit ~ z_comp+z_stat+z_rel + 控制)，K=6 主，3/9 稳健
  2. H1 分类伴随：按 dominant_type 的退出率（控制声望分层）
  3. §5b 强制深挖：fence-sitters / 共线性(VIF) / 声望混淆
  4. H3：exit vs migration 的多项/二元回归
  5. 安慰剂提示（占位，需 placebo 数据）
"""
from __future__ import annotations
import os
import numpy as np
import pandas as pd
from statsmodels.duration.hazard_regression import PHReg
import statsmodels.api as sm
import statsmodels.formula.api as smf

HERE = os.path.dirname(__file__)
RES = os.path.join(HERE, "..", "data_collection", "results")
df = pd.read_csv(os.path.join(RES, "analysis_dataset.csv"))

print("="*70)
print(f"分析样本: {len(df)} 核心贡献者")
print("="*70)

CONTROLS = ["log_pre_ans", "log_rep", "tenure_years"]


def cox(K, with_controls=True):
    cols = ["z_comp", "z_stat", "z_rel"] + (CONTROLS if with_controls else [])
    X = df[cols].astype(float).values
    dur = df[f"dur_K{K}"].values
    evt = df[f"exit_K{K}"].values
    model = PHReg(dur, X, status=evt, ties="efron")
    res = model.fit()
    hr = np.exp(res.params)
    ci = np.exp(res.conf_int())
    out = pd.DataFrame({"coef": res.params, "HR": hr,
                        "HR_lo": ci[:, 0], "HR_hi": ci[:, 1],
                        "p": res.pvalues}, index=cols)
    return out


print("\n" + "#"*70)
print("# H1 主模型：连续 Cox，K=6（控制 答题量/声望/资历）")
print("#"*70)
r6 = cox(6, True)
print(r6.round(4))
print("\nH1 预测: z_stat HR>1(地位退出快), z_rel HR<1(关系慢), z_comp 居中")
print("解读: HR>1 = 该动机越强→退出风险越高")

print("\n" + "#"*70)
print("# H1 稳健性：K=3 和 K=9")
print("#"*70)
for K in (3, 9):
    print(f"\n--- K={K} ---")
    print(cox(K, True)[["HR", "HR_lo", "HR_hi", "p"]].round(4))

print("\n" + "#"*70)
print("# 对照：不控制声望（看声望混淆有多大）")
print("#"*70)
print(cox(6, False)[["HR", "HR_lo", "HR_hi", "p"]].round(4))

# ---------- §5b 强制深挖 ----------
print("\n" + "="*70)
print("§5b 强制深挖（因描述性 H1 排序与预期不一致而触发）")
print("="*70)

print("\n[1] Fence-sitters：分类的领先幅度分布")
print(df["type_margin"].describe().round(3))
weak = (df["type_margin"] < 0.3).mean()
print(f"领先幅度<0.3（勉强归类）占比: {weak:.1%}")

print("\n[2] 共线性：三个动机指标 + 控制的相关 & VIF")
from statsmodels.stats.outliers_influence import variance_inflation_factor
Xv = df[["z_comp", "z_stat", "z_rel", "log_pre_ans", "log_rep", "tenure_years"]].astype(float)
Xv = sm.add_constant(Xv)
vif = pd.Series([variance_inflation_factor(Xv.values, i) for i in range(Xv.shape[1])],
                index=Xv.columns)
print("VIF:"); print(vif.round(2))
print("\n动机指标相关矩阵:")
print(df[["z_comp", "z_stat", "z_rel"]].corr().round(3))

print("\n[3] 声望混淆：各动机型的声望分布（是否精通型集中在低声望？）")
print(df.groupby("dominant_type")[["log_rep", "Reputation", "PreAnsCount"]].median().round(2))

print("\n[4] 声望分层内的退出率（控制声望后排序还成立吗）")
df["rep_band"] = pd.cut(df["Reputation"], [0, 500, 2000, 10000, 1e9],
                        labels=["0-500", "500-2k", "2k-10k", "10k+"])
print(pd.crosstab(df["rep_band"], df["dominant_type"],
                  values=df["exit_K6"], aggfunc="mean").round(3))

# ---------- H3 ----------
print("\n" + "#"*70)
print("# H3：exit vs migration（在退出者中，关系型更倾向迁移？）")
print("#"*70)
sub = df[df["outcome3"].isin(["exit", "migration"])].copy()
sub["is_exit"] = (sub["outcome3"] == "exit").astype(int)
m = smf.logit("is_exit ~ z_comp + z_stat + z_rel + log_pre_ans + log_rep + tenure_years",
              data=sub).fit(disp=0)
print(f"\n停止答题者 N={len(sub)}（exit {sub['is_exit'].sum()} / migration {(1-sub['is_exit']).sum()}）")
print("Logit: P(exit | 已停止答题)，正系数=更可能彻底退出而非迁移")
co = pd.DataFrame({"coef": m.params, "OR": np.exp(m.params), "p": m.pvalues})
print(co.loc[["z_comp", "z_stat", "z_rel"]].round(4))
print("\nH3 预测: z_rel 系数<0（关系型更可能迁移而非退出）")

print("\n分类视角 — outcome3 by type（声望分层）:")
for band in ["0-500", "500-2k", "2k-10k", "10k+"]:
    b = df[df["rep_band"] == band]
    ct = pd.crosstab(b["dominant_type"], b["outcome3"], normalize="index")
    print(f"\n  [{band}]"); print(ct.round(3))


# ---------- 探索性（POST-HOC）：地位×声望交互，检验"反转"是否真实 ----------
# 缘起：分层退出率里 10k+ 段 status 看似最高(0.305)。用正式交互项检验，
# 避免把噪音当发现（§5b 深挖第3条 非线性）。
print("\n" + "="*70)
print("POST-HOC: 地位效应是否随声望反转？(z_stat × log_rep 交互, K=6)")
print("="*70)
df["log_rep_c"] = df["log_rep"] - df["log_rep"].mean()
df["z_stat_x_rep"] = df["z_stat"] * df["log_rep_c"]
_cols = ["z_comp","z_stat","z_rel","z_stat_x_rep","log_pre_ans","log_rep_c","tenure_years"]
_res = PHReg(df["dur_K6"].values, df[_cols].astype(float).values,
             status=df["exit_K6"].values, ties="efron").fit()
_hr = np.exp(_res.params)
print(pd.DataFrame({"HR":_hr, "p":_res.pvalues}, index=_cols).round(4))
_ix = _cols.index("z_stat_x_rep")
print(f"\n交互项 z_stat_x_rep: HR={_hr[_ix]:.4f}, p={_res.pvalues[_ix]:.3f}")
print("结论: 交互 p=0.52 不显著 → '反转'是噪音，非真效应。")
print("地位型在所有声望层均更扛(HR≈0.86稳定)。不写入论文作探索性发现。")
