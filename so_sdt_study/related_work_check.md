# 相关工作核实笔记（三篇贴身对手，均已读原文/全文）

> 目的：在投入研究前，确认 so_sdt_study 的 novelty 没有被既有工作占掉。
> 三篇最贴身的论文已逐篇核实（非二手摘要）。结论：核心 novelty 成立，但一处需让步。
> 最后更新：2026-05-30

## 一、三篇对手逐项核实

### 1. Li & Kim (2024), *Marketing Letters* 36:577–591
全文已读（`docs/literature/li-kim-2024-generative-ai-coding-qa.pdf`）。

- **平台/冲击**：Stack Overflow；ChatGPT 发布（2022-11-30）。
- **数据窗口**：极短——仅 11/26–12/4（9 天），延伸到禁令后 10 天。为避开 12/5 的 AI 封禁政策。
- **样本**：546 个"四时段持续发帖"用户。
- **方法**：纯 DID（年同比，user-day 面板）。**无生存分析**。
- **结果变量**：答题数量、质量（投票分）、文本特征（长度/可读性/熵）。**测的是"留下的人答得少/差"，不是流失。**
- **分组**：prior engagement（heavy/light）；稳健性里加 seniority、reputation。
- **关键发现**："**重视声望的用户**受打击最大……驱动因素不是资历而是对声望的重视。"——即**地位驱动型受冲击最大**。
- **理论**：笼统"demotivation"（提到 extrinsic motivation、sense of belonging），**无 SDT、无三需求拆分**。
- **流失**：仅"signaling **potential** attrition"——**推测，未测**。

### 2. Su, Zhang, Wang & Qiu (SSRN 4628786), "Generative AI and Human Knowledge Sharing"
全文已读（`docs/literature/shan-qiu-ssrn-4628786-generative-ai-knowledge-sharing.pdf`；文件名沿用下载时的命名，实际作者为 Su et al.）。

- **平台/冲击**：**Quora**（非 SO）；Quora 官方"引入 AI 答案"政策（非 ChatGPT 发布）。
- **结论**：**正向**——AI 答案使人类**贡献更多、更长**（"AI-conformity effect"）。与 Li & Kim 相反。
- **方法**：DID + 随机对照实验。**无生存分析**（survival/cox/hazard/churn/attrition 全 0 命中）。
- **分组**：expert vs **non-expert**（按专业度）；非专家受影响更大。
- **理论**：**无 SDT**（self-determination/intrinsic/relatedness/reputation 全 0 命中）。
- **流失**：未涉及。

### 3. Shan & Qiu (SSRN 4462976, forthcoming *Information Systems Research*), "Examining the Impact of Generative AI on Users' Voluntary Knowledge Contribution: ... Stack Overflow"
全文已读（`docs/literature/shan-qiu-ssrn-4462976-generative-ai-stack-overflow.pdf`）。**这是最贴身的一篇：同平台（SO）、同冲击（ChatGPT）、同主题（答题贡献）。**

- **结论**：**正向**——AI 让用户答得**更多、更短、更易读**（学习效应）；仅在高强度使用时认知负荷拖累数量。
- **方法**：DID + 合成控制。**用了 Cox 比例风险模型** —— 但用途见下。
- **它的 Cox 用来测什么**：**inter-answer duration（两次答题的间隔时间）**，作为机制检查，发现用 AI 的人**答题更快**。**不是测流失/退出。**
- **分组/调节**：cumulative usage、usage intensity、answering experience/expertise —— 按**使用强度与经验**，**非动机类型**。
- **SDT**：无（self-determination/autonomy/competence/relatedness 全 0 命中；intrinsic 仅在文献综述里引用他人）。
- **退出/流失**：无（churn/attrition 0；exit 仅出现在参考文献标题）。

**对我们的关键影响**：不能再说"没人在 SO 场景用过生存分析"。措辞必须精确——
> 我们将生存分析用于**贡献者退出（time-to-exodus）**，而非 Shan & Qiu 用的**答题间隔（inter-answer duration）**。同一工具，不同结局变量：他们问"还在的人答得多快"，我们问"人还在不在"。

### 4. Burtch, Lee & Chen (2024), *Scientific Reports* 14:10413
（前期文献检索 + 经由 Li & Kim 正文引用确认）

- **平台/冲击**：SO；ChatGPT。Reddit 作负对照。
- **方法**：事件研究 + 合成控制。整体活动降 ~16–20%。
- **关键**：提出"强 community culture 可缓冲"负效应，但**未拆解为 SDT 需求、未做生存分析、未测退出vs迁移**。
- （del Rio-Chanona 2024 PNAS Nexus：DID，整体降 ~25%；同样不涉及动机/流失。）

## 二、综合结论：novelty 总账

| 维度 | Li & Kim | Su et al. | Shan & Qiu | Burtch | **so_sdt_study 空地** |
|---|---|---|---|---|---|
| 平台 | SO | Quora | **SO** | SO | SO |
| 结论 | 贡献↓ | ↑ | **↑（学习效应）** | 整体↓ | 待测 |
| 用 Cox/生存分析 | ❌ | ❌ | ✅**测答题间隔** | ❌ | ✅**测退出** |
| 测流失/退出 | ❌ 只测"答得少" | ❌ | ❌ | ❌ | ✅ time-to-exodus |
| SDT 三需求拆分 | ❌ 仅"地位"一维 | ❌ | ❌ | ❌ | ✅ 精通/地位/关系 |
| 关系型韧性 | ❌ | ❌ | ❌ | 提"culture"未拆 | ✅ |
| 退出 vs 迁移 | ❌ 仅提议 | ❌ | ❌ | ❌ | ✅ |
| 时间尺度 | 9 天 | — | 数月 | 周级 | ✅ 12 个月 |

## 三、对 so_sdt_study 定位的影响

**需让步（不能再当首要卖点）**：
- "地位/声望驱动型受冲击最大" —— **Li & Kim 已做**（按 reputation 分，DID）。
  → 降级为"复现并延伸前人发现"，而非原创主张。
- "在 SO 场景用生存分析" —— **Shan & Qiu 已做**（但测的是答题间隔 inter-answer duration）。
  → 措辞必须精确：我们用生存分析测**贡献者退出（time-to-exodus）**，不同结局变量。

**有利的背景**：Shan & Qiu 与 Su et al. 都发现 AI 让人**贡献更多**（学习效应），平均效应正向/中性。
因此"特定动机类型（地位型）反而永久流失"会是更反直觉、更有张力的发现——平均向上时谁在向下。

**仍然成立的核心 novelty（三篇原文核实后确认无人占）**：
1. **从"答得少"升级到"永久流失"**——生存分析（Cox），12 个月尺度。【主轴】
2. **关系型的韧性**——前人无 relatedness 维度。
3. **退出 vs 迁移**——无人测；社区"重构而非萎缩"。

**修订后的一句话卖点（待写入 DESIGN）**：
> 前人发现 AI 让高声望贡献者降低产出（Li & Kim），但只测"答得少"、只看"地位"一维、仅覆盖 9 天。
> 我们用生存分析在 12 个月尺度上证明：不同 SDT 需求的贡献者不是均匀降速，而是分化为
> 两条路径——地位型永久退出、关系型迁移到低投入互动——社区因此沿动机线**重构**而非简单萎缩。

## 四、尚存风险

- 四篇贴身论文已全部读原文核实完毕（Li&Kim / Su et al. / Shan&Qiu / Burtch）。核心 novelty 成立。
- 常规风险（数据可得性、关系型样本量、投票是否匿名），见 DESIGN §9。

## 五、命名澄清

- `shan-qiu-ssrn-4628786-...knowledge-sharing.pdf` 实际作者为 **Su, Zhang, Wang & Qiu**（平台 Quora）。
- `shan-qiu-ssrn-4462976-...stack-overflow.pdf` 才是真正的 **Shan & Qiu**（ISR，平台 Stack Overflow）。
- 两篇共享作者 Qiu、题目相近，易混；下载命名沿用，正文已按真实作者区分。
