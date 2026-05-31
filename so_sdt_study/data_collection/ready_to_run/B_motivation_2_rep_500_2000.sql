-- =====================================================================
-- 第一批 / 查询 B：每个核心贡献者的【动机指标明细】（分型主输入）
-- =====================================================================
-- 运行：https://data.stackexchange.com/stackoverflow/query/new
-- 下载 → 存为：batch1_preshock/B_motivation_indices__<分片>.csv
--
-- ⛔ 只用冲击前数据(2021-11-30..2022-11-29)。这是分型输入，冻结前/后都可取。
--
-- 这是查询 A(聚合)的【明细版】：每个入组用户一行，导出算三个 SDT 动机指标
-- 所需的【原始分量】。分析端(Claude)据此做 z 标准化 + 连续/分类分型。
-- 用 UserId 作为与第二批(B1/B2)合并的主键。
--
-- 导出的是原始分量(不在 SQL 里做 z 标准化)，因为 z 要在全体上算，
-- 分片导出后由 Claude 在本地合并所有片再统一标准化。
--
-- 分片(按 Reputation，与第二批对齐)：
--   片1: 0..500  片2: 500..2000  片3: 2000..10000  片4: 10000..up
-- =====================================================================

DECLARE @ClassStart datetime = '2021-11-30';
DECLARE @ClassEnd   datetime = '2022-11-30';
DECLARE @TenureCut  datetime = '2022-08-31';

-- ===== 分片 =====
DECLARE @RepLo int = 500;
DECLARE @RepHi int = 2000;
-- ================

WITH PreAns AS (
    SELECT p.Id, p.OwnerUserId AS UserId, p.ParentId AS QId, p.CreationDate
    FROM Posts p
    WHERE p.PostTypeId = 2
      AND p.CreationDate >= @ClassStart AND p.CreationDate < @ClassEnd
      AND p.OwnerUserId IS NOT NULL
),
Cohort AS (
    SELECT pa.UserId, COUNT(*) AS AnsCount, u.Reputation
    FROM PreAns pa
    JOIN Users u ON u.Id = pa.UserId
    WHERE u.CreationDate <= @TenureCut
      AND u.Reputation >= @RepLo AND u.Reputation < @RepHi
    GROUP BY pa.UserId, u.Reputation
    HAVING COUNT(*) >= 5
),
QInfo AS (
    SELECT q.Id AS QId, q.AnswerCount, q.Score AS QScore
    FROM Posts q WHERE q.PostTypeId = 1
),
-- 精通分量：答难题占比 + 答"零答案"开荒题占比
Comp AS (
    SELECT pa.UserId,
           AVG(CASE WHEN qi.AnswerCount <= 1 THEN 1.0 ELSE 0.0 END) AS HardShare,
           COUNT(*) AS nAns
    FROM PreAns pa JOIN QInfo qi ON qi.QId = pa.QId
    GROUP BY pa.UserId
),
-- 地位分量：答热门题(>=3答案)占比 + 自己答案的平均分(声望累积)
Stat AS (
    SELECT pa.UserId,
           AVG(CASE WHEN qi.AnswerCount >= 3 THEN 1.0 ELSE 0.0 END) AS CrowdShare
    FROM PreAns pa JOIN QInfo qi ON qi.QId = pa.QId
    GROUP BY pa.UserId
),
-- 关系分量：评论/答题比 + 编辑他人帖数
Rel AS (
    SELECT c.UserId, COUNT(*) AS PreComments
    FROM Comments c
    WHERE c.CreationDate >= @ClassStart AND c.CreationDate < @ClassEnd
      AND c.UserId IS NOT NULL
    GROUP BY c.UserId
),
RelEdit AS (
    SELECT ph.UserId, COUNT(*) AS PreEditsOthers
    FROM PostHistory ph
    JOIN Posts p ON p.Id = ph.PostId
    WHERE ph.CreationDate >= @ClassStart AND ph.CreationDate < @ClassEnd
      AND ph.PostHistoryTypeId IN (4,5,6)
      AND ph.UserId IS NOT NULL
      AND (p.OwnerUserId IS NULL OR p.OwnerUserId <> ph.UserId)
    GROUP BY ph.UserId
)
SELECT
    c.UserId,
    c.Reputation,
    c.AnsCount,
    cmp.HardShare              AS CompetenceProxy,   -- 精通
    stt.CrowdShare             AS StatusProxy,       -- 地位
    CAST(ISNULL(rl.PreComments,0) AS float)/c.AnsCount AS RelCommentRatio, -- 关系1
    ISNULL(re.PreEditsOthers,0) AS RelEditsOthers    -- 关系2
FROM Cohort c
LEFT JOIN Comp    cmp ON cmp.UserId = c.UserId
LEFT JOIN Stat    stt ON stt.UserId = c.UserId
LEFT JOIN Rel     rl  ON rl.UserId  = c.UserId
LEFT JOIN RelEdit re  ON re.UserId  = c.UserId
ORDER BY c.UserId;

-- 分析端：合并所有分片 → z 标准化每个 proxy → 连续指标进 Cox(主)
--   + argmax 分类(伴随)。关系指标由 RelCommentRatio + RelEditsOthers 合成。
