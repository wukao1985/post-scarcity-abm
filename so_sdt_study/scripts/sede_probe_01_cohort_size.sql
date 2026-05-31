-- =====================================================================
-- so_sdt_study — 探查查询 #1：冻结前样本量与动机型分布勘探
-- =====================================================================
--
-- 运行方式：复制到 https://data.stackexchange.com/stackoverflow/query/new
--          点 "Run Query"（免费、无需登录、几秒出结果）。
--
-- ⛔ 纪律红线（必须遵守）：
--   本查询只统计【冲击前】窗口（2021-11-30 .. 2022-11-29）的用户与行为。
--   绝不触碰 2022-11-30 之后的任何数据。
--   目的是回答："有多少核心贡献者可被分类？三种动机型各多少人？
--   关系型够不够撑统计？" —— 不是 "谁离开了"。
--   结局（谁退出）要等设计冻结后才能碰。
--
-- 它回答三件事：
--   (A) 符合入组的核心贡献者总数（冲击前 >=5 答题、注册满 3 个月）
--   (B) 按三个粗动机指标分型后，每型的人数 —— 尤其关系型够不够
--   (C) 关键指标的分布（中位数/分位数），看指标有没有区分度
--
-- 注意：这里的指标是【粗版】，只为勘探样本量，不是最终冻结的分型公式。
--       最终公式在 DESIGN.md §5，更细。这里故意从简，先看人数。
-- =====================================================================

DECLARE @ClassStart datetime = '2021-11-30';
DECLARE @ClassEnd   datetime = '2022-11-29';   -- 冲击前一天，绝不跨过
DECLARE @TenureCut  datetime = '2022-08-31';   -- 冲击时至少注册 3 个月

-- 冲击前窗口内的答题（answers: PostTypeId = 2）
WITH PreAnswers AS (
    SELECT p.Id          AS AnswerId,
           p.OwnerUserId AS UserId,
           p.ParentId    AS QuestionId,
           p.CreationDate,
           p.Score
    FROM Posts p
    WHERE p.PostTypeId = 2
      AND p.CreationDate >= @ClassStart
      AND p.CreationDate <  @ClassEnd
      AND p.OwnerUserId IS NOT NULL
),
-- 入组用户：冲击前 >=5 答题 且 注册满 3 个月
Cohort AS (
    SELECT pa.UserId,
           COUNT(*)            AS AnsCount,
           AVG(CAST(pa.Score AS float)) AS AvgScore
    FROM PreAnswers pa
    JOIN Users u ON u.Id = pa.UserId
    WHERE u.CreationDate <= @TenureCut
    GROUP BY pa.UserId
    HAVING COUNT(*) >= 5
),
-- 粗动机指标（仅勘探用）：
--   关系型代理 = 冲击前窗口内该用户的评论数 / 答题数
--   精通型代理 = 答到"难题"的比例（难题 = 该问题最终答案数 <= 1）
--   地位型代理 = 答到"已有 >=3 答案的热门题"的比例（抢边际声望）
CommentCnt AS (
    SELECT c.UserId, COUNT(*) AS CmtCount
    FROM Comments c
    WHERE c.CreationDate >= @ClassStart
      AND c.CreationDate <  @ClassEnd
      AND c.UserId IS NOT NULL
    GROUP BY c.UserId
),
QAnsCount AS (   -- 每个被回答问题，最终有多少答案（难度代理）
    SELECT q.Id AS QuestionId, q.AnswerCount
    FROM Posts q
    WHERE q.PostTypeId = 1
),
UserStyle AS (
    SELECT pa.UserId,
           AVG(CASE WHEN qa.AnswerCount <= 1 THEN 1.0 ELSE 0.0 END) AS HardShare,
           AVG(CASE WHEN qa.AnswerCount >= 3 THEN 1.0 ELSE 0.0 END) AS CrowdShare
    FROM PreAnswers pa
    JOIN QAnsCount qa ON qa.QuestionId = pa.QuestionId
    GROUP BY pa.UserId
),
Enriched AS (
    SELECT co.UserId,
           co.AnsCount,
           ISNULL(cc.CmtCount, 0)                               AS CmtCount,
           CAST(ISNULL(cc.CmtCount,0) AS float) / co.AnsCount   AS RelatednessProxy,
           us.HardShare                                         AS CompetenceProxy,
           us.CrowdShare                                        AS StatusProxy
    FROM Cohort co
    LEFT JOIN CommentCnt cc ON cc.UserId = co.UserId
    LEFT JOIN UserStyle  us ON us.UserId = co.UserId
),
-- 标准化后取 argmax 作粗分型（z-score 用全体均值/标准差近似）
Stats AS (
    SELECT AVG(RelatednessProxy) AS rM, STDEV(RelatednessProxy) AS rS,
           AVG(CompetenceProxy)  AS cM, STDEV(CompetenceProxy)  AS cS,
           AVG(StatusProxy)      AS sM, STDEV(StatusProxy)      AS sS
    FROM Enriched
),
Typed AS (
    SELECT e.*,
           (e.RelatednessProxy - s.rM) / NULLIF(s.rS,0) AS zRel,
           (e.CompetenceProxy  - s.cM) / NULLIF(s.cS,0) AS zComp,
           (e.StatusProxy      - s.sM) / NULLIF(s.sS,0) AS zStat
    FROM Enriched e CROSS JOIN Stats s
)
SELECT
    CASE
        WHEN zRel >= zComp AND zRel >= zStat THEN 'relatedness'
        WHEN zComp >= zRel AND zComp >= zStat THEN 'competence'
        ELSE 'status'
    END AS DominantType,
    COUNT(*)                         AS NumUsers,
    AVG(AnsCount)                    AS AvgAnswers,
    AVG(RelatednessProxy)            AS AvgRelProxy,
    AVG(CompetenceProxy)             AS AvgCompProxy,
    AVG(StatusProxy)                 AS AvgStatusProxy
FROM Typed
GROUP BY
    CASE
        WHEN zRel >= zComp AND zRel >= zStat THEN 'relatedness'
        WHEN zComp >= zRel AND zComp >= zStat THEN 'competence'
        ELSE 'status'
    END
ORDER BY NumUsers DESC;

-- =====================================================================
-- 看结果时关注：
--   1. 三型 NumUsers 加起来 = 入组核心贡献者总数（应是几万量级 → 充足）
--   2. relatedness 那一行的 NumUsers —— 如果只有几百，关系型是风险点，
--      要在 DESIGN 里调整（放宽关系型定义 / 或承认关系型样本受限）
--   3. 三型的 AvgRelProxy / AvgCompProxy / AvgStatusProxy 是否互相区分 ——
--      如果每型在自己那个指标上明显更高，说明分型有区分度
-- =====================================================================
