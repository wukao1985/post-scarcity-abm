# 取数执行清单（给研究者）

设计已冻结。按下面顺序在 SEDE 上跑查询、下 CSV、commit。Claude 负责合并与分析。

SEDE 地址：https://data.stackexchange.com/stackoverflow/query/new
（粘贴 SQL → Run Query → 结果下方 Download CSV）

---

## 分片说明（重要）

SO 有 ~5 万核心贡献者，SEDE 单次约 5 万行上限。所以 B、B1、B2 三个**明细**查询都要
**按声望分 4 片**跑。每个 .sql 顶部有 `@RepLo / @RepHi` 两行，每片改一次：

| 片 | @RepLo | @RepHi | 文件名后缀 |
|---|---|---|---|
| 1 | 0 | 500 | `__rep_0_500.csv` |
| 2 | 500 | 2000 | `__rep_500_2000.csv` |
| 3 | 2000 | 10000 | `__rep_2000_10000.csv` |
| 4 | 10000 | 99999999 | `__rep_10000_up.csv` |

跑前看 SEDE 返回行数：若某片 > 5 万行（被截断），把该片再二分（如 0..200 / 200..500）。
**截断很危险**——会悄悄丢数据。每片跑完确认行数 < 5 万。

---

## 执行顺序

### 第一批（分型输入，冲击前数据）

**① `batch1_preshock/B_motivation_indices_per_user.sql`** — 跑 4 片
存：`batch1_preshock/B_motivation_indices__rep_0_500.csv` 等 4 个文件。

（查询 A 的聚合结果已有，无需重跑。）

### 第二批（结局，冲击后数据）

**② `batch2_outcomes/B1_exodus_per_user.sql`** — 跑 4 片
存：`batch2_outcomes/B1_exodus__rep_0_500.csv` 等 4 个。

**③ `batch2_outcomes/B2_migration_per_user.sql`** — 跑 4 片
存：`batch2_outcomes/B2_migration__rep_0_500.csv` 等 4 个。

---

## 合并的主键

三组数据都按 `UserId` 导出、用相同声望分片，Claude 在本地按 UserId join：
B(动机指标) + B1(退出) + B2(迁移) → 每个贡献者一行完整记录 → 进 Cox。

所以**务必三个查询用相同的声望区间分片**，否则对不齐。

---

## 完成后

12 个 CSV（3 查询 × 4 片）commit + push。告诉 Claude，开始分析：
合并 → z 标准化 → Cox 生存分析(K=3/6/9) → H3 退出vs迁移 → 出图出结论。

CSV 都不大（每片几万行、纯数字/ID），可直接入 git。
