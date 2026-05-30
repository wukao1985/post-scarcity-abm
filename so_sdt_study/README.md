# so_sdt_study — AI 冲击下在线社群贡献者的差异化流失（实证研究）

> 这是本仓库 **新方向** 的工作目录。它与旧的 ABM 后稀缺模拟（`models/`、`reports/paper_draft.md` 等）**完全隔离**，互不依赖。旧路线的状态见 `../tasks/todo.md` 顶部说明。

## 这个研究在做什么（一句话）

用 ChatGPT 冲击（2022-11-30）这个**真实发生的自然实验**，检验一个**可证伪**的预测：
按 Stack Overflow 用户在冲击**前**行为体现的**动机类型**（精通驱动 / 地位驱动 / 关系驱动）分组后，
冲击**后**的流失率是否呈 **地位型 > 精通型 > 关系型**——并且在控制了冲击前活动量后依然成立。

## 为什么从 ABM 转到这里

旧的 ABM 论文（post-labor behavioral sink）经过 ~20 轮评审，卡在两个无法治愈的结构性问题上：
1. **循环论证**：核心结论几乎是被 meaning 函数的定义直接推出来的，不是模型"发现"的。
2. **不可证伪**：模拟一个假想的 80% 失业未来，没有 ground truth，永远只能是思辨。

文献扫描（见下）确认：AI 对在线社群的**活动量影响**已被顶刊做透，但**没有人**从
自我决定论（SDT）/ 意义感角度，用真实行为数据检验"哪种动机最先被 AI 替代掉"。
这个缝隙是真实的、novel 的、且用公开数据够得着——适合独立研究者。

## 核心文档

- **`DESIGN.md`** ← **先读这个**。预注册式设计文档：假说、用户分型怎么操作化、识别策略、
  可证伪标准、安慰剂检验、分析计划。**关键纪律：所有分型规则在碰任何冲击后数据之前冻结。**

## 数据

- 公开 Stack Exchange 数据转储（2025-12-31 社区版，archive.org / communitydatadump.com）
- 字段齐全：Users / Posts / Votes / Comments / Badges / PostHistory / Tags
- 备选：BigQuery 公共数据集（免费额度够探查），SEDE（在线 SQL）
- 详见 `scripts/` 下的下载与探查脚手架

## 目录结构

```
so_sdt_study/
├── DESIGN.md          # 预注册设计文档（核心）
├── README.md          # 本文件
├── scripts/
│   ├── download_data.py    # 数据获取脚手架
│   └── explore_signal.py   # 信号探查脚手架（先验证"动机×差异化流失"信号是否存在）
└── data/              # 本地数据（gitignore，不入库）
```

## 已确立的相关文献（避免重复造轮子）

- del Rio-Chanona, Laurentsyeva & Wachs (2024, *PNAS Nexus*) — SO 活动降 ~25%，DiD
- Burtch, Lee & Chen (2024, *Scientific Reports*) — 降 ~16–20%，事件研究，Reddit 负对照
- Quinn & Gutt (2025, *JMIS*) — 异质性：休闲用户降 ~18%，核心用户基本不变（**按活动量分，非按动机分**）
- Helic & Santos (2025, arXiv) — 简单问题减少、难问题翻倍
- 机制证据（实验室）：Nature *Sci. Rep.* 2025/2026（AI 削弱内在动机/自我效能/意义感）；CHI 2026

## 当前状态

🟡 **设计阶段。** 设计文档草稿已成。下一步：搭好数据 pipeline，先在小站点上验证
"动机类型 × 差异化流失"这个信号到底存不存在，再决定是否全量投入。
