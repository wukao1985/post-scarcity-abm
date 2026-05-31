-- =====================================================================
-- 第一批 / 查询 A：核心贡献者样本量 + 三型分布（聚合，一次出结果）
-- =====================================================================
-- 运行：https://data.stackexchange.com/stackoverflow/query/new
-- 下载结果 → 存为：so_sdt_study/data_collection/batch1_preshock/A_cohort_size_aggregate.csv
--
-- ⛔ 只碰冲击前数据（2021-11-30 .. 2022-11-29）。不查冲击后。
--
-- 目的：立刻回答"SO 上符合入组的核心贡献者有多少？按三种动机型粗分各多少人？
--      关系型够不够撑统计？" —— 聚合输出，不导明细，几行结果。
--
-- 这是【粗版】分型，只为勘探样本量。最终冻结公式见 DESIGN.md §5。
-- =====================================================================

DECLARE @ClassStart datetime = '2021-11-30';
DECLARE @ClassEnd   datetime = '2022-11-30';   -- 严格小于此 = 冲击前
DECLARE @TenureCut  datetime = '2022-08-31';   -- 注册满 ~3 个月

-- 冲击前的答题
WITH PreAns AS (
    SELECT p.Id, p.OwnerUserId AS UserId, p.ParentId AS QId
    FROM Posts p
    WHERE p.PostTypeId = 2
      AND p.CreationDate >= @ClassStart
      AND p.CreationDate <  @ClassEnd
      AND p.OwnerUserId IS NOT NULL
),
-- 入组：冲击前 >=5 答题 且 注册满 3 个月
Cohort AS (
    SELECT pa.UserId, COUNT(*) AS AnsCount
    FROM PreAns pa
    JOIN Users u ON u.Id = pa.UserId
    WHERE u.CreationDate <= @TenureCut
    GROUP BY pa.UserId
    HAVING COUNT(*) >= 5
),
-- 关系型代理：冲击前评论数 / 答题数
Cmt AS (
    SELECT c.UserId, COUNT(*) AS CmtCount
    FROM Comments c
    WHERE c.CreationDate >= @ClassStart
      AND c.CreationDate <  @ClassEnd
      AND c.UserId IS NOT NULL
    GROUP BY c.UserId
),
-- 难度/热门代理：被回答问题最终的答案数
QInfo AS (
    SELECT q.Id AS QId, q.AnswerCount
    FROM Posts q WHERE q.PostTypeId = 1
),
Style AS (
    SELECT pa.UserId,
           AVG(CASE WHEN qi.AnswerCount <= 1 THEN 1.0 ELSE 0.0 END) AS HardShare,   -- 精通代理
           AVG(CASE WHEN qi.AnswerCount >= 3 THEN 1.0 ELSE 0.0 END) AS CrowdShare    -- 地位代理
    FROM PreAns pa JOIN QInfo qi ON qi.QId = pa.QId
    GROUP BY pa.UserId
),
Enriched AS (
    SELECT co.UserId, co.AnsCount,
           CAST(ISNULL(cm.CmtCount,0) AS float)/co.AnsCount AS RelProxy,
           ISNULL(st.HardShare,0)  AS CompProxy,
           ISNULL(st.CrowdShare,0) AS StatProxy
    FROM Cohort co
    LEFT JOIN Cmt   cm ON cm.UserId = co.UserId
    LEFT JOIN Style st ON st.UserId = co.UserId
),
Stat AS (
    SELECT AVG(RelProxy) rM, STDEV(RelProxy) rS,
           AVG(CompProxy) cM, STDEV(CompProxy) cS,
           AVG(StatProxy) sM, STDEV(StatProxy) sS
    FROM Enriched
),
Typed AS (
    SELECT e.*,
           (e.RelProxy  - s.rM)/NULLIF(s.rS,0) AS zR,
           (e.CompProxy - s.cM)/NULLIF(s.cS,0) AS zC,
           (e.StatProxy - s.sM)/NULLIF(s.sS,0) AS zS
    FROM Enriched e CROSS JOIN Stat s
)
SELECT
    CASE WHEN zR>=zC AND zR>=zS THEN 'relatedness'
         WHEN zC>=zR AND zC>=zS THEN 'competence'
         ELSE 'status' END                AS DominantType,
    COUNT(*)                              AS NumUsers,
    AVG(AnsCount)                         AS AvgAnswers,
    AVG(RelProxy)                         AS AvgRelProxy,
    AVG(CompProxy)                        AS AvgCompProxy,
    AVG(StatProxy)                        AS AvgStatProxy
FROM Typed
GROUP BY
    CASE WHEN zR>=zC AND zR>=zS THEN 'relatedness'
         WHEN zC>=zR AND zC>=zS THEN 'competence'
         ELSE 'status' END
ORDER BY NumUsers DESC;

-- 期望看到：三行（competence / status / relatedness），NumUsers 加总 = 入组总数。
-- 关注：relatedness 那行人数是否够（>几千 = 好；几百 = 风险，需调关系型定义）。
