"""Exploratory sensitivity check, NOT pre-registered (added 2026-11-16, after results).

Question: do the headline cross-section results survive dropping the GSS 2021-2024 waves?
Those waves changed survey mode (mostly web/mail instead of face-to-face), which can shift
answers to "happy" and "life exciting". Re-uses the exact model code of analyze.py.

Usage:  python3 -I mode_sensitivity.py /path/to/gssr/data > ../results/mode_sensitivity.json
"""
import sys, json, os
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "analyze.py")).read()
head = src.split("    # ---- confirmatory cross-section")[0]
ns = {"__name__": "mode_sens"}
sys.argv = [sys.argv[0]] + sys.argv[1:]
exec(compile(head, "analyze.py[head]", "exec"), ns)
d_all = ns["d"]
res = {"note": "exploratory, not pre-registered; years <= 2018 only (pre mode change)"}
for label, mask in (("all_years", d_all.year > 0), ("le_2018", d_all.year <= 2018)):
    ns["d"] = d_all[mask].copy()
    r = {"n_rows": int(len(ns["d"]))}
    r["H1_O1"] = ns["base_model"]("O1")["penalty"]
    r["H1_O2b"] = ns["base_model"]("O2b")["penalty"]
    full = ns["d"]
    for code, name in ((4, "unemployed"), (5, "retired_lt65")):
        ns["d"] = full[full.wrkstat.isin([1, 2, 3, code])].copy()
        r[f"S1_{name}_O1"] = ns["base_model"]("O1")["penalty"]
        r[f"S1_{name}_O2b"] = ns["base_model"]("O2b")["penalty"]
    ns["d"] = full
    for M in ("M3", "M2"):
        r[f"{M}_O2b_buffer"] = ns["moderator_model"]("O2b", M)["buffer(M1-M0)"]
    res[label] = r
print(json.dumps(res, indent=1, ensure_ascii=False, default=float))
