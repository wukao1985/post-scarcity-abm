# 数据采集说明（SEDE 路径）

> 给研究者（你）的操作手册。Claude 负责分析，你负责用 SEDE 把数据取进 repo。

## 为什么走 SEDE

- Stack Overflow 全量转储解压后 100GB+，进不了 git，也进不了 Claude 的容器（环境网络策略封死了 archive.org / SEDE / BigQuery）。
- 但**你那边**网络是通的。SEDE（Stack Exchange Data Explorer）让你在线跑 SQL、直接下载 CSV，无需下载任何大文件。
- 我们只需要一个**子集**（两年、去正文、结构化字段），几十 MB 量级，能 commit 进 repo。

## ⛔ 纪律红线（关乎论文诚信，必须遵守）

**分两批取数，顺序不能乱：**

- **第一批（现在）= 只取冲击前数据**（2021-11-30 之前）。用于：数样本量、构建动机分型。
  → 见 `batch1_preshock/`
- **第二批（设计冻结后才取）= 冲击后结局数据**。用于：测谁退出、退出vs迁移。
  → 见 `batch2_outcomes/`（设计冻结前**不要**跑）

为什么：分型公式必须在看任何冲击后结局之前冻结。否则就是 p-hacking，整篇论文的"可证伪"卖点就毁了。

## 操作步骤（每个 .sql 文件）

1. 打开 https://data.stackexchange.com/stackoverflow/query/new
2. 把 .sql 文件内容整个复制进去
3. 点 **Run Query**（几秒~几十秒）
4. 结果下方点 **Download CSV**
5. 把 CSV 存到对应目录，文件名**严格按 .sql 文件头注释里指定的名字**
6. `git add` + `commit` + `push`（CSV 不大，可直接入库）

## 命名与存放

```
so_sdt_study/data_collection/
├── README.md            ← 本文件
├── batch1_preshock/     ← 第一批 SQL + 你下载的 CSV
└── batch2_outcomes/     ← 第二批（冻结后才动）
```

CSV 命名规范：`<查询名>__<分片标识>.csv`，例如 `cohort_typed__rep_lt500.csv`。
具体名字每个 .sql 文件头部都写明了。

## SEDE 的限制（我已据此设计查询）

- 单次查询结果约 **5 万行上限**。超了的查询我已按声望区间分片（你多跑几次、各下一个 CSV）。
- 查询有超时（几分钟）。若超时，.sql 里有备注怎么缩小范围。
- 投票（Votes）在 SO 公开数据里是匿名的（无 UserId），所以我们不依赖它。
