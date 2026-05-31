-- =====================================================================
-- 安慰剂检验 / 合并查询：假冲击 2021-11-30（真冲击前一年）
-- =====================================================================
-- 运行：https://data.stackexchange.com/stackoverflow/query/new
-- 下载 → 存为：results/placebo_<片>.csv
--
-- 目的：把整套分析平移到 ChatGPT 之前一年。若"关系型迁移而非退出"(H3)
--   在这个【没有 AI】的假冲击处也出现 → H3 的因果解释破产；
--   若不出现 → H3 由 ChatGPT 驱动，成立。
--
-- 所有时间窗 = 真研究 - 1 年：
--   分类窗 2020-11-30 .. 2021-11-29  (重新分型)
--   假冲击 2021-11-30
--   结局窗 2022-02-01 .. 2022-11-29  (9个月,停在真冲击前,干净)
--
-- 合并：一个查询同时出 分型指标 + 退出 + 迁移（精简为4片，按声望）。
--
-- 分片(与真研究对齐): 片1:0-500 片2:500-2000 片3:2000-10000 片4:10000+
-- =====================================================================

DECLARE @ClassStart datetime = '2020-11-30';
DECLARE @ClassEnd   datetime = '2021-11-30';
DECLARE @TenureCut  datetime = '2021-08-31';
DECLARE @OutStart   datetime = '2022-02-01';
DECLARE @OutEnd     datetime = '2022-11-30';   -- 停在真冲击前

-- ===== 分片 =====
DECLARE @RepLo int = 2000;
DECLARE @RepHi int = 10000;
-- ================

WITH PreAns AS (
    SELECT p.Id, p.OwnerUserId AS UserId, p.ParentId AS QId
    FROM Posts p
    WHERE p.PostTypeId = 2
      AND p.CreationDate >= @ClassStart AND p.CreationDate < @ClassEnd
      AND p.OwnerUserId IS NOT NULL
),
Cohort AS (
    SELECT pa.UserId, COUNT(*) AS PreAnsCount, u.Reputation,
           DATEDIFF(day, u.CreationDate, @ClassEnd) AS AccountAgeDays
    FROM PreAns pa
    JOIN Users u ON u.Id = pa.UserId
    WHERE u.CreationDate <= @TenureCut
      AND u.Reputation >= @RepLo AND u.Reputation < @RepHi
    GROUP BY pa.UserId, u.Reputation, u.CreationDate
    HAVING COUNT(*) >= 5
),
QInfo AS (SELECT q.Id AS QId, q.AnswerCount FROM Posts q WHERE q.PostTypeId = 1),
-- 分型指标（假分类窗）
Style AS (
    SELECT pa.UserId,
           AVG(CASE WHEN qi.AnswerCount <= 1 THEN 1.0 ELSE 0.0 END) AS CompetenceProxy,
           AVG(CASE WHEN qi.AnswerCount >= 3 THEN 1.0 ELSE 0.0 END) AS StatusProxy
    FROM PreAns pa JOIN QInfo qi ON qi.QId = pa.QId
    GROUP BY pa.UserId
),
PreCmt AS (
    SELECT c.UserId, COUNT(*) AS PreComments
    FROM Comments c
    WHERE c.CreationDate >= @ClassStart AND c.CreationDate < @ClassEnd AND c.UserId IS NOT NULL
    GROUP BY c.UserId
),
PreEdit AS (
    SELECT ph.UserId, COUNT(*) AS PreEditsOthers
    FROM PostHistory ph JOIN Posts p ON p.Id = ph.PostId
    WHERE ph.CreationDate >= @ClassStart AND ph.CreationDate < @ClassEnd
      AND ph.PostHistoryTypeId IN (4,5,6) AND ph.UserId IS NOT NULL
      AND (p.OwnerUserId IS NULL OR p.OwnerUserId <> ph.UserId)
    GROUP BY ph.UserId
),
-- 假结局窗：退出（最后答题）
PostAns AS (
    SELECT p.OwnerUserId AS UserId, MAX(p.CreationDate) AS LastAnswerAfter, COUNT(*) AS PostAnsTotal
    FROM Posts p
    WHERE p.PostTypeId = 2 AND p.CreationDate >= @OutStart AND p.CreationDate < @OutEnd
      AND p.OwnerUserId IS NOT NULL
    GROUP BY p.OwnerUserId
),
-- 假结局窗：迁移（评论+编辑他人）
PostCmt AS (
    SELECT c.UserId, COUNT(*) AS PostComments
    FROM Comments c
    WHERE c.CreationDate >= @OutStart AND c.CreationDate < @OutEnd AND c.UserId IS NOT NULL
    GROUP BY c.UserId
),
PostEdit AS (
    SELECT ph.UserId, COUNT(*) AS PostEdits
    FROM PostHistory ph JOIN Posts p ON p.Id = ph.PostId
    WHERE ph.CreationDate >= @OutStart AND ph.CreationDate < @OutEnd
      AND ph.PostHistoryTypeId IN (4,5,6) AND ph.UserId IS NOT NULL
      AND (p.OwnerUserId IS NULL OR p.OwnerUserId <> ph.UserId)
    GROUP BY ph.UserId
)
SELECT
    c.UserId, c.Reputation, c.AccountAgeDays, c.PreAnsCount,
    st.CompetenceProxy, st.StatusProxy,
    CAST(ISNULL(pc.PreComments,0) AS float)/c.PreAnsCount AS RelCommentRatio,
    ISNULL(pe.PreEditsOthers,0) AS RelEditsOthers,
    pa.LastAnswerAfter,
    ISNULL(pa.PostAnsTotal,0)   AS PostAnsTotal,
    ISNULL(poc.PostComments,0)  AS PostComments,
    ISNULL(poe.PostEdits,0)     AS PostEdits
FROM Cohort c
LEFT JOIN Style    st  ON st.UserId  = c.UserId
LEFT JOIN PreCmt   pc  ON pc.UserId  = c.UserId
LEFT JOIN PreEdit  pe  ON pe.UserId  = c.UserId
LEFT JOIN PostAns  pa  ON pa.UserId  = c.UserId
LEFT JOIN PostCmt  poc ON poc.UserId = c.UserId
LEFT JOIN PostEdit poe ON poe.UserId = c.UserId
ORDER BY c.UserId;
