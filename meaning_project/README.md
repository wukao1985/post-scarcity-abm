# meaning_project — 中枢 (the hub)

Medium 写作的中枢。终身项目：**后 AI / 后劳动时代的人类意义**。

每次新 session，让 Claude 先读 `MANIFESTO.md` + `STYLE.md` + 当前在写的文章，就能接上。
（Claude 的记忆每次重置，这个 repo 是长期记忆。）

## 文件
- **`SYNTHESIS.md`** — **核心活文档**：对"AI 后劳动时代意义"全部理解的分层总述。按子问题
  （Q1–Q13）组织，每个标注当前在🟢/🟡/🔴哪层、依据、缺口、如何升级。一切从这里生长、回流到这里。
  文章是它的枝叶，数据让它升级。
- **`MANIFESTO.md`** — 项目纲领：核心问题、三层诚实方法论(🟢实证/🟡类比/🔴设计)、niche、成功的样子。**北极星。**
- **`evidence_base.md`** — 🟢 经验地基清单（Jahoda、UBI实验、绝望之死、SO零结果…）。文章引用🟢要追溯到这里。
- **`idea_pool.md`** — 选题池。养想法、挑成熟的、诚实地砍掉弱的。
- **`concepts.md`** — 项目自己的概念/框架（随写作积累，目标是别人能引用的招牌概念）。
- **`STYLE.md`** — 文风 + Medium 规范 + 诚实铁律 + 每篇的工作流。
- **`articles/`** — 每篇 Medium 一个文件夹（brief → 证据/图 → draft → 发表）。

## 怎么用（每次想写文章）
回来说一句"我想写一篇关于 X 的"，Claude 会：
1. 读 MANIFESTO/STYLE 对齐 → 在 `articles/<slug>/brief.md` 起选题简报（角度、claim 类型主线、核心takeaway、用哪些🟢锚点）
2. 需要的话跑个小分析/出图当🟢支柱
3. 写 `draft.md` → 按诚实铁律打磨
4. 发表后标记、记 URL

## 第一篇推荐
《How to honestly talk about the future of AI — a three-layer framework》
立方法论招牌，用 SO 零结果当"让数据推翻假设"的真实案例。

## 血脉
脱胎于本 repo 两个前身：不可证伪的 post-scarcity ABM（已归档 `../archive/abm_v1/`，教训：打磨≠修地基）；
可证伪的 SO 零结果研究 `../so_sdt_study/`（证明能做诚实实证，可当🟢支柱/案例）。
