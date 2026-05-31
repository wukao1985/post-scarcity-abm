-- =====================================================================
-- 第二批 / 查询 B1：每个核心贡献者的【退出】数据（生存分析主输入）
-- =====================================================================
-- 运行：https://data.stackexchange.com/stackoverflow/query/new
-- 下载 → 存为：batch2_outcomes/B1_exodus_per_user__<分片>.csv
--
-- ✅ 设计已冻结（DESIGN.md, 2026-05-30），现在允许取冲击后数据。
--
-- 输出：每个入组用户一行，含
--   UserId, Reputation, AccountAge(天), 冲击前答题数,
--   冲击后最后一次答题日期(LastAnswerAfter), 冲击后总答题数,
--   各阶段(0-3 / 3-6 / 6-12 月)答题数 —— 供 Cox 算 time-to-exodus 用。
--
-- ⚠️ SEDE 约 5 万行上限。我们有 ~5 万贡献者 → 必须分片。
--    用 @RepLo/@RepHi 按声望区间分片，多跑几次、每次下一个 CSV。
--    建议分片（按 Reputation）：
--      片1: 0    .. 500      文件名 ..__rep_0_500.csv
--      片2: 500  .. 2000     ..__rep_500_2000.csv
--      片3: 2000 .. 10000    ..__rep_2000_10000.csv
--      片4: 10000.. 99999999 ..__rep_10000_up.csv
--    （每片应 < 5 万行；若某片仍超，再二分。跑前看返回行数。）
-- =====================================================================

DECLARE @ClassStart  datetime = '2021-11-30';
DECLARE @ClassEnd    datetime = '2022-11-30';   -- 冲击前
DECLARE @TenureCut   datetime = '2022-08-31';
DECLARE @Shock       datetime = '2022-11-30';
DECLARE @WashoutEnd  datetime = '2023-02-01';   -- 结局从此开始计
DECLARE @DataEnd     datetime = '2024-02-01';   -- 结局窗结束(12个月)

-- ===== 改这两行做分片 =====
DECLARE @RepLo int = 0;
DECLARE @RepHi int = 500;        -- [@RepLo, @RepHi)
-- ==========================

WITH PreAns AS (
    SELECT p.OwnerUserId AS UserId, COUNT(*) AS PreAnsCount
    FROM Posts p
    WHERE p.PostTypeId = 2
      AND p.CreationDate >= @ClassStart AND p.CreationDate < @ClassEnd
      AND p.OwnerUserId IS NOT NULL
    GROUP BY p.OwnerUserId
),
Cohort AS (   -- 入组 + 声望分片
    SELECT pa.UserId, pa.PreAnsCount, u.Reputation,
           DATEDIFF(day, u.CreationDate, @Shock) AS AccountAgeDays
    FROM PreAns pa
    JOIN Users u ON u.Id = pa.UserId
    WHERE pa.PreAnsCount >= 5
      AND u.CreationDate <= @TenureCut
      AND u.Reputation >= @RepLo AND u.Reputation < @RepHi
),
-- 冲击后(洗脱期后)的答题，按用户聚合
PostAns AS (
    SELECT p.OwnerUserId AS UserId,
           MAX(p.CreationDate) AS LastAnswerAfter,
           COUNT(*)            AS PostAnsTotal,
           SUM(CASE WHEN p.CreationDate <  DATEADD(month,3,@WashoutEnd) THEN 1 ELSE 0 END) AS Ans_0_3,
           SUM(CASE WHEN p.CreationDate >= DATEADD(month,3,@WashoutEnd)
                     AND p.CreationDate <  DATEADD(month,6,@WashoutEnd) THEN 1 ELSE 0 END) AS Ans_3_6,
           SUM(CASE WHEN p.CreationDate >= DATEADD(month,6,@WashoutEnd) THEN 1 ELSE 0 END) AS Ans_6_12
    FROM Posts p
    WHERE p.PostTypeId = 2
      AND p.CreationDate >= @WashoutEnd AND p.CreationDate < @DataEnd
      AND p.OwnerUserId IS NOT NULL
    GROUP BY p.OwnerUserId
)
SELECT
    c.UserId,
    c.Reputation,
    c.AccountAgeDays,
    c.PreAnsCount,
    pa.LastAnswerAfter,                         -- NULL = 冲击后从未答题(立即退出)
    ISNULL(pa.PostAnsTotal,0) AS PostAnsTotal,
    ISNULL(pa.Ans_0_3,0)      AS Ans_0_3,
    ISNULL(pa.Ans_3_6,0)      AS Ans_3_6,
    ISNULL(pa.Ans_6_12,0)     AS Ans_6_12
FROM Cohort c
LEFT JOIN PostAns pa ON pa.UserId = c.UserId
ORDER BY c.UserId;

-- 分析端(Claude)据此算：
--   exit_time = LastAnswerAfter 与 @WashoutEnd 的间隔；若长期无答题(gap>=K月)判为退出，
--   gap 用阶段答题数交叉验证；K=3/6/9 三套全跑(DESIGN §6)。
--   LastAnswerAfter 为 NULL = 冲击后即退出(survival time = 0)。
