"""
本地管线验证脚本。

目的：用一份【真实的中型 Stack Exchange 站点 XML dump】（从 GitHub 公开镜像
clone 而来）在本地验证整套分析逻辑——解析 → 入组 → 三个 SDT 动机指标 →
z 标准化 → argmax 分型。确认 SQL/分析逻辑无 bug，再让研究者去 SEDE 上对
Stack Overflow 跑等价查询。

这证明了"分析端可由 Claude 在容器内完全自闭环"：只要数据 XML/CSV 进了
仓库，从解析到分型到（后续）Cox 生存分析，全部可在此环境独立完成。

用法：
    # 先 clone 一个真实 SE 站点 dump（GitHub 在本环境可达；archive.org 不可达）
    git clone --depth 1 <github-mirror-of-some-SE-site> /tmp/se_dump
    python validate_pipeline_local.py /tmp/se_dump

注意：此脚本用于【逻辑验证】，不是正式分析。正式分析对象是 Stack Overflow
（数据经 SEDE 由研究者导出、commit 进 repo）。时间窗在正式运行时改回
DESIGN.md §3 冻结的 2021-11-30..2022-11-29 分类窗。
"""
from __future__ import annotations
import sys, os
import xml.etree.ElementTree as ET
from collections import defaultdict, Counter
import statistics as st

# 分类窗（验证时可按数据实际范围调整；正式分析用 DESIGN 冻结值）
CLASS_START = os.environ.get("CLASS_START", "2021-11-30")
CLASS_END   = os.environ.get("CLASS_END",   "2022-11-30")   # 严格小于 = 冲击前
TENURE_CUT  = os.environ.get("TENURE_CUT",  "2022-08-31")
MIN_ANSWERS = int(os.environ.get("MIN_ANSWERS", "5"))


def iter_rows(path):
    for _, el in ET.iterparse(path, events=("end",)):
        if el.tag == "row":
            yield el.attrib
        el.clear()


def run(dump_dir: str):
    P = lambda f: os.path.join(dump_dir, f)

    ureg = {a["Id"]: a.get("CreationDate", "")[:10] for a in iter_rows(P("Users.xml"))}

    qac = {}           # question id -> final answer count (difficulty proxy)
    answers = []       # (uid, qid) in class window
    for a in iter_rows(P("Posts.xml")):
        pt = a.get("PostTypeId")
        if pt == "1":
            qac[a["Id"]] = int(a.get("AnswerCount", 0))
        elif pt == "2":
            cd = a.get("CreationDate", "")[:10]
            uid = a.get("OwnerUserId")
            if uid and CLASS_START <= cd < CLASS_END:
                answers.append((uid, a.get("ParentId")))

    cmt = defaultdict(int)
    for a in iter_rows(P("Comments.xml")):
        cd = a.get("CreationDate", "")[:10]; uid = a.get("UserId")
        if uid and CLASS_START <= cd < CLASS_END:
            cmt[uid] += 1

    acount = Counter(u for u, _ in answers)
    cohort = {u for u, c in acount.items()
              if c >= MIN_ANSWERS and ureg.get(u, "9999") <= TENURE_CUT}

    by_user = defaultdict(list)
    for u, q in answers:
        if u in cohort:
            by_user[u].append(q)

    rel, comp, stat = {}, {}, {}
    for u, qs in by_user.items():
        rel[u]  = cmt.get(u, 0) / acount[u]
        comp[u] = sum(1 for q in qs if qac.get(q, 0) <= 1) / len(qs)
        stat[u] = sum(1 for q in qs if qac.get(q, 0) >= 3) / len(qs)

    def zscore(d):
        v = list(d.values()); m = st.mean(v); s = st.pstdev(v) or 1.0
        return {k: (x - m) / s for k, x in d.items()}

    zr, zc, zs = zscore(rel), zscore(comp), zscore(stat)
    typ = Counter()
    for u in cohort:
        a, b, c = zr[u], zc[u], zs[u]
        if a >= b and a >= c: typ["relatedness"] += 1
        elif b >= a and b >= c: typ["competence"] += 1
        else: typ["status"] += 1

    print(f"dump: {dump_dir}")
    print(f"window: {CLASS_START} .. {CLASS_END}  (>= {MIN_ANSWERS} answers)")
    print(f"cohort (core contributors): {len(cohort)}")
    print(f"type distribution: {dict(typ)}")
    if rel:
        print(f"median relatedness proxy (comments/answer): {st.median(rel.values()):.3f}")
        print(f"median competence proxy (hard-question share): {st.median(comp.values()):.3f}")
        print(f"median status proxy (crowded-question share): {st.median(stat.values()):.3f}")
    print("\nOK: parse -> cohort -> 3 indices -> z-score -> argmax typing all run.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python validate_pipeline_local.py <dump_dir with *.xml>")
        sys.exit(1)
    run(sys.argv[1])
