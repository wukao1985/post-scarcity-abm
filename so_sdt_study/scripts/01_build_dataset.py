"""
01 — 合并 12 个 CSV，构建分析数据集（分型 + 结局），冻结设计 DESIGN.md。

输入：data_collection/results/{B_motivation,B1_exodus,B2_migration}_{1..4}.csv
输出：data_collection/results/analysis_dataset.csv  (每核心贡献者一行)

严格按冻结设计：
- 动机指标 z 标准化（在全体上算）→ 连续主 + argmax 分类伴随
- 结局：time-to-exodus（K=3/6/9 月）+ exit vs migration
- 关系指标 = RelCommentRatio 与 RelEditsOthers 各自 z 后取均值
"""
from __future__ import annotations
import os, glob
import numpy as np
import pandas as pd

HERE = os.path.dirname(__file__)
RES = os.path.join(HERE, "..", "data_collection", "results")

SHOCK_TO_OUTCOME_END_MONTHS = 12  # 结局窗 2023-02 .. 2024-02


def load_shards(prefix):
    parts = [pd.read_csv(os.path.join(RES, f"{prefix}_{i}.csv")) for i in (1, 2, 3, 4)]
    df = pd.concat(parts, ignore_index=True)
    df = df.drop_duplicates(subset="UserId")
    return df


def zscore(s):
    s = s.astype(float)
    sd = s.std(ddof=0)
    return (s - s.mean()) / (sd if sd > 0 else 1.0)


def main():
    mot = load_shards("B_motivation")   # UserId,Reputation,AnsCount,CompetenceProxy,StatusProxy,RelCommentRatio,RelEditsOthers
    exo = load_shards("B1_exodus")      # UserId,Reputation,AccountAgeDays,PreAnsCount,LastAnswerAfter,PostAnsTotal,Ans_0_3,Ans_3_6,Ans_6_12
    mig = load_shards("B2_migration")   # UserId,PostComments,PreComments,PostEdits

    print(f"shards loaded: motivation {len(mot)}, exodus {len(exo)}, migration {len(mig)}")

    df = mot.merge(exo, on="UserId", suffixes=("", "_exo")).merge(mig, on="UserId")
    print(f"merged cohort: {len(df)} users")

    # ---- 动机指标 z 标准化 ----
    df["z_comp"] = zscore(df["CompetenceProxy"])
    df["z_stat"] = zscore(df["StatusProxy"])
    # 关系 = 两个分量各自 z 后平均
    df["z_rel"] = (zscore(df["RelCommentRatio"]) + zscore(df["RelEditsOthers"])) / 2.0
    df["z_rel"] = zscore(df["z_rel"])  # 再标准化使量纲一致

    # ---- 分类伴随：argmax ----
    z = df[["z_comp", "z_stat", "z_rel"]].values
    types = np.array(["competence", "status", "relatedness"])
    df["dominant_type"] = types[z.argmax(axis=1)]
    # 领先幅度（用于 §5b fence-sitter 诊断）
    zs = np.sort(z, axis=1)
    df["type_margin"] = zs[:, -1] - zs[:, -2]

    # ---- 结局：退出时间 ----
    # LastAnswerAfter 为空 = 冲击后(洗脱期后)从未答题 = survival time 0（立即退出）
    last = pd.to_datetime(df["LastAnswerAfter"], errors="coerce")
    outcome_start = pd.Timestamp("2023-02-01")
    outcome_end = pd.Timestamp("2024-02-01")
    # 最后答题距洗脱期开始的月数（活跃时长）；空=0
    active_months = (last - outcome_start).dt.days / 30.44
    df["active_months"] = active_months.fillna(0.0).clip(lower=0.0)
    # 观测总时长（用于删失）
    total_months = (outcome_end - outcome_start).days / 30.44  # ~12

    # 三个 K 阈值各算一套 (event=退出, duration=生存时长)
    for K in (3, 6, 9):
        # 退出 = 最后答题后沉默 >= K 月（即 active_months <= total_months - K 视为已退出）
        # duration = active_months（最后一次答题的时点）；event=1 若之后沉默到数据末满 K 月
        silence = total_months - df["active_months"]
        df[f"exit_K{K}"] = (silence >= K).astype(int)
        # 生存时长：退出者=active_months；未退出(删失)=total_months
        df[f"dur_K{K}"] = np.where(df[f"exit_K{K}"] == 1, df["active_months"], total_months)

    # ---- H3：exit vs migration（在 K=6 的退出者里分）----
    df["post_engage"] = df["PostComments"] + df["PostEdits"]   # 迁移信号(评论+编辑他人)
    stopped = df["exit_K6"] == 1
    df["outcome3"] = np.where(
        ~stopped, "active",
        np.where(df["post_engage"] > 0, "migration", "exit"))

    # ---- 控制变量 ----
    df["log_pre_ans"] = np.log1p(df["PreAnsCount"])
    df["log_rep"] = np.log1p(df["Reputation"])
    df["tenure_years"] = df["AccountAgeDays"] / 365.25

    out = os.path.join(RES, "analysis_dataset.csv")
    keep = ["UserId", "Reputation", "log_rep", "PreAnsCount", "log_pre_ans",
            "tenure_years", "AnsCount",
            "z_comp", "z_stat", "z_rel", "dominant_type", "type_margin",
            "active_months", "post_engage",
            "exit_K3", "dur_K3", "exit_K6", "dur_K6", "exit_K9", "dur_K9",
            "outcome3"]
    df[keep].to_csv(out, index=False)
    print(f"\nwrote {out}  ({len(df)} rows)")

    # ---- 快速健康检查 ----
    print("\n=== 分型分布 ===")
    print(df["dominant_type"].value_counts())
    print("\n=== 退出率（K=6） by 动机型 ===")
    print(df.groupby("dominant_type")["exit_K6"].mean().round(3))
    print("\n=== outcome3（退出vs迁移） by 动机型 ===")
    print(pd.crosstab(df["dominant_type"], df["outcome3"], normalize="index").round(3))


if __name__ == "__main__":
    main()
