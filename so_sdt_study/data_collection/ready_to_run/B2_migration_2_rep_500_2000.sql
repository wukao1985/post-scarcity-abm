-- =====================================================================
-- 第二批 / 查询 B2：每个核心贡献者的【迁移】数据（H3 输入）
-- =====================================================================
-- 运行：https://data.stackexchange.com/stackoverflow/query/new
-- 下载 → 存为：batch2_outcomes/B2_migration_per_user__<分片>.csv
--
-- ✅ 设计已冻结。冲击后数据。
--
-- 目的：H3 = 区分"退出"(停答题且停一切) vs "迁移"(停答题但转向评论/编辑)。
-- 输出：每个入组用户冲击后(洗脱期后)的【评论数】和【编辑他人帖数】。
--   配合 B1 的答题数，分析端判定每人是 exit 还是 migration。
--
-- 注意：投票(Votes)在 SO 公开数据中匿名(无 UserId)，无法追踪 → 不用。
--   迁移信号 = 评论 + 编辑他人帖(PostHistory)。
--
-- 同样按声望分片(与 B1 用相同区间，便于对齐合并)。
--   片1: 0..500  片2: 500..2000  片3: 2000..10000  片4: 10000..up
-- =====================================================================

DECLARE @ClassStart  datetime = '2021-11-30';
DECLARE @ClassEnd    datetime = '2022-11-30';
DECLARE @TenureCut   datetime = '2022-08-31';
DECLARE @Shock       datetime = '2022-11-30';
DECLARE @WashoutEnd  datetime = '2023-02-01';
DECLARE @DataEnd     datetime = '2024-02-01';

-- ===== 改这两行做分片(与 B1 对齐) =====
DECLARE @RepLo int = 500;
DECLARE @RepHi int = 2000;
-- ======================================

WITH PreAns AS (
    SELECT p.OwnerUserId AS UserId, COUNT(*) AS PreAnsCount
    FROM Posts p
    WHERE p.PostTypeId = 2
      AND p.CreationDate >= @ClassStart AND p.CreationDate < @ClassEnd
      AND p.OwnerUserId IS NOT NULL
    GROUP BY p.OwnerUserId
),
Cohort AS (
    SELECT pa.UserId
    FROM PreAns pa
    JOIN Users u ON u.Id = pa.UserId
    WHERE pa.PreAnsCount >= 5
      AND u.CreationDate <= @TenureCut
      AND u.Reputation >= @RepLo AND u.Reputation < @RepHi
),
-- 冲击后评论数(迁移信号 1)
PostCmt AS (
    SELECT c.UserId, COUNT(*) AS PostComments
    FROM Comments c
    WHERE c.CreationDate >= @WashoutEnd AND c.CreationDate < @DataEnd
      AND c.UserId IS NOT NULL
    GROUP BY c.UserId
),
-- 冲击前评论数(算迁移"增量"用，基线)
PreCmt AS (
    SELECT c.UserId, COUNT(*) AS PreComments
    FROM Comments c
    WHERE c.CreationDate >= @ClassStart AND c.CreationDate < @ClassEnd
      AND c.UserId IS NOT NULL
    GROUP BY c.UserId
),
-- 冲击后编辑他人帖(迁移信号 2)：PostHistory 中由该用户发起、且非本人作者的编辑
-- PostHistoryTypeId 4,5,6 = Edit Title/Body/Tags
PostEdit AS (
    SELECT ph.UserId, COUNT(*) AS PostEdits
    FROM PostHistory ph
    JOIN Posts p ON p.Id = ph.PostId
    WHERE ph.CreationDate >= @WashoutEnd AND ph.CreationDate < @DataEnd
      AND ph.PostHistoryTypeId IN (4,5,6)
      AND ph.UserId IS NOT NULL
      AND (p.OwnerUserId IS NULL OR p.OwnerUserId <> ph.UserId)   -- 编辑他人的帖
    GROUP BY ph.UserId
)
SELECT
    c.UserId,
    ISNULL(pc.PostComments,0)  AS PostComments,
    ISNULL(prc.PreComments,0)  AS PreComments,
    ISNULL(pe.PostEdits,0)     AS PostEdits
FROM Cohort c
LEFT JOIN PostCmt  pc  ON pc.UserId  = c.UserId
LEFT JOIN PreCmt   prc ON prc.UserId = c.UserId
LEFT JOIN PostEdit pe  ON pe.UserId  = c.UserId
ORDER BY c.UserId;

-- 分析端(Claude)据此 + B1 的答题数判定：
--   stopped_answering(B1, K月无答题) AND (PostComments=0 AND PostEdits=0) → EXIT
--   stopped_answering AND (PostComments>0 OR PostEdits>0)                  → MIGRATION
--   not stopped → ACTIVE
