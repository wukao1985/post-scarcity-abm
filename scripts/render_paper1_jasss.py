#!/usr/bin/env python3
from __future__ import annotations

import html
import math
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
MANUSCRIPT_PATH = REPORTS_DIR / "paper_draft.md"
HTML_OUTPUT_PATH = REPORTS_DIR / "paper_jasss_submission.html"
CSS_PATH = REPO_ROOT / "scripts" / "paper1_jasss.css"

MANUSCRIPT_FIGURES = {
    1: FIGURES_DIR / "paper1_jasss_figure_1.png",
    2: FIGURES_DIR / "paper1_jasss_figure_2.png",
    3: FIGURES_DIR / "paper1_jasss_figure_3.png",
    4: FIGURES_DIR / "paper1_jasss_figure_4.png",
    5: FIGURES_DIR / "paper1_jasss_figure_5.png",
    6: FIGURES_DIR / "paper1_jasss_figure_6.png",
    7: FIGURES_DIR / "paper1_jasss_figure_7.png",
    8: FIGURES_DIR / "paper1_jasss_figure_8.png",
}

FIGURES_BY_SECTION = {
    "3.1": [1],
    "3.2": [2],
    "3.3": [3],
    "3.5": [4],
    "3.6": [5],
    "3.7": [6, 7],
    "3.8": [8],
}

ROUTE_A_FACTORS = [
    ("factor_income", "Income support"),
    ("factor_fairness", "Fairness"),
    ("factor_role_participation", "Role participation"),
    ("factor_autonomy", "Autonomy"),
    ("factor_competence", "Competence"),
    ("factor_relatedness", "Relatedness"),
    ("factor_status", "Status"),
    ("factor_contribution", "Contribution"),
]


def manuscript_figure_path(number: int) -> str:
    return f"figures/{MANUSCRIPT_FIGURES[number].name}"


def configure_plotting() -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Georgia", "Times New Roman", "DejaVu Serif"],
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 9,
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "savefig.facecolor": "white",
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )


def save_figure(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(path, bbox_inches="tight")
    plt.close()


def generate_figure_1() -> None:
    df = pd.read_csv(REPO_ROOT / "data" / "simulation" / "sweep1_results.csv")
    baseline = df[df["scenario"] == "baseline"]
    grouped = (
        baseline.groupby("post_labor")
        .agg(
            social_distress=("sink_index", "mean"),
            social_distress_sem=("sink_index", "sem"),
            collapse_probability=("sink_collapsed", "mean"),
            collapse_probability_sem=("sink_collapsed", "sem"),
        )
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(7.0, 4.6))
    ax.plot(
        grouped["post_labor"],
        grouped["social_distress"],
        color="#1d4f8c",
        linewidth=2.4,
        marker="o",
        label="Social distress",
    )
    ax.fill_between(
        grouped["post_labor"],
        grouped["social_distress"] - 1.96 * grouped["social_distress_sem"],
        grouped["social_distress"] + 1.96 * grouped["social_distress_sem"],
        color="#1d4f8c",
        alpha=0.18,
    )
    ax.plot(
        grouped["post_labor"],
        grouped["collapse_probability"],
        color="#8c2d04",
        linewidth=2.2,
        marker="s",
        linestyle="--",
        label="Collapse probability",
    )
    ax.fill_between(
        grouped["post_labor"],
        grouped["collapse_probability"] - 1.96 * grouped["collapse_probability_sem"],
        grouped["collapse_probability"] + 1.96 * grouped["collapse_probability_sem"],
        color="#8c2d04",
        alpha=0.12,
    )
    ax.axvspan(0.80, 0.95, color="#d9d9d9", alpha=0.25)
    ax.set_xlabel("Displacement target")
    ax.set_ylabel("Population share / probability")
    ax.set_ylim(0, 1.02)
    ax.set_xlim(grouped["post_labor"].min() - 0.01, grouped["post_labor"].max() + 0.01)
    ax.set_title("Baseline threshold zone")
    ax.legend(loc="upper left")
    save_figure(MANUSCRIPT_FIGURES[1])


def compute_route_a_main_effects() -> pd.DataFrame:
    df = pd.read_csv(REPO_ROOT / "reports" / "route_a_results" / "route_a_summary.csv")
    rows = []
    for factor_col, label in ROUTE_A_FACTORS:
        off = df[df[factor_col] == 0]
        on = df[df[factor_col] == 1]
        rows.append(
            {
                "factor": label,
                "social_distress_effect": on["mean_social_distress"].mean() - off["mean_social_distress"].mean(),
                "collapse_probability_effect": on["collapse_probability"].mean() - off["collapse_probability"].mean(),
                "meaning_effect": on["mean_meaning"].mean() - off["mean_meaning"].mean(),
            }
        )
    result = pd.DataFrame(rows)
    order = (
        result.assign(order_value=result["social_distress_effect"].abs())
        .sort_values("order_value", ascending=True)["factor"]
        .tolist()
    )
    return result.set_index("factor").loc[order].reset_index()


def generate_figure_2() -> None:
    effects = compute_route_a_main_effects()
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 6.9), sharex=False)
    colors = ["#ba3c2f" if value > 0 else "#2b6cb0" for value in effects["social_distress_effect"]]
    axes[0].barh(effects["factor"], effects["social_distress_effect"], color=colors)
    axes[0].axvline(0, color="#666666", linewidth=0.8)
    axes[0].set_title("Main effects on mean social distress")
    axes[0].set_xlabel("Effect of turning factor on")

    colors = ["#ba3c2f" if value > 0 else "#2b6cb0" for value in effects["collapse_probability_effect"]]
    axes[1].barh(effects["factor"], effects["collapse_probability_effect"], color=colors)
    axes[1].axvline(0, color="#666666", linewidth=0.8)
    axes[1].set_title("Main effects on collapse probability")
    axes[1].set_xlabel("Effect of turning factor on")

    fig.suptitle("Route A orthogonal sweep at post-labour fraction 0.95", y=0.98, fontsize=13)
    plt.tight_layout()
    save_figure(MANUSCRIPT_FIGURES[2])


def compute_route_a_interactions() -> pd.DataFrame:
    df = pd.read_csv(REPO_ROOT / "reports" / "route_a_results" / "route_a_summary.csv")
    interactions = []
    for i, (factor_a, label_a) in enumerate(ROUTE_A_FACTORS):
        for factor_b, label_b in ROUTE_A_FACTORS[i + 1 :]:
            mean_00 = df[(df[factor_a] == 0) & (df[factor_b] == 0)]["mean_social_distress"].mean()
            mean_01 = df[(df[factor_a] == 0) & (df[factor_b] == 1)]["mean_social_distress"].mean()
            mean_10 = df[(df[factor_a] == 1) & (df[factor_b] == 0)]["mean_social_distress"].mean()
            mean_11 = df[(df[factor_a] == 1) & (df[factor_b] == 1)]["mean_social_distress"].mean()
            interaction = (mean_11 - mean_10) - (mean_01 - mean_00)
            interactions.append(
                {
                    "pair": f"{label_a} × {label_b}",
                    "interaction": interaction,
                    "abs_interaction": abs(interaction),
                }
            )
    return pd.DataFrame(interactions).sort_values("abs_interaction", ascending=False).head(10)


def generate_figure_3() -> None:
    interactions = compute_route_a_interactions().sort_values("abs_interaction", ascending=True)
    colors = ["#2f6b2f" if value >= 0 else "#7a1f1f" for value in interactions["interaction"]]
    fig, ax = plt.subplots(figsize=(7.6, 5.2))
    ax.barh(interactions["pair"], interactions["interaction"], color=colors)
    ax.axvline(0, color="#666666", linewidth=0.8)
    ax.set_xlabel("Interaction effect on mean social distress")
    ax.set_title("Top two-way Route A interactions")
    save_figure(MANUSCRIPT_FIGURES[3])


def generate_figure_4() -> None:
    df = pd.read_csv(REPO_ROOT / "data" / "simulation" / "sweep3_virtual_world.csv")
    baseline = df[df["scenario"] == "baseline"]

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.5))
    for pl, color, marker in [(0.8, "#2b6cb0", "o"), (0.95, "#ba3c2f", "s")]:
        subset = baseline[baseline["post_labor"] == pl]
        grouped = subset.groupby("virtual_world_quality").agg(
            social_distress=("sink_index", "mean"),
            social_distress_sem=("sink_index", "sem"),
            collapse_probability=("sink_collapsed", "mean"),
            collapse_probability_sem=("sink_collapsed", "sem"),
        )
        axes[0].plot(grouped.index, grouped["social_distress"], color=color, marker=marker, linewidth=2, label=f"PL={pl}")
        axes[0].fill_between(
            grouped.index,
            grouped["social_distress"] - 1.96 * grouped["social_distress_sem"],
            grouped["social_distress"] + 1.96 * grouped["social_distress_sem"],
            color=color,
            alpha=0.15,
        )
        axes[1].plot(grouped.index, grouped["collapse_probability"], color=color, marker=marker, linewidth=2, label=f"PL={pl}")
        axes[1].fill_between(
            grouped.index,
            np.clip(grouped["collapse_probability"] - 1.96 * grouped["collapse_probability_sem"], 0, 1),
            np.clip(grouped["collapse_probability"] + 1.96 * grouped["collapse_probability_sem"], 0, 1),
            color=color,
            alpha=0.12,
        )

    axes[0].set_title("Mean social distress")
    axes[1].set_title("Collapse probability")
    for ax in axes:
        ax.set_xlabel("Virtual-world quality")
        ax.set_ylim(0, 1.02)
        ax.legend()
    plt.tight_layout()
    save_figure(MANUSCRIPT_FIGURES[4])


def generate_figure_5() -> None:
    df = pd.read_csv(REPO_ROOT / "data" / "simulation" / "sweep4_collectivism.csv")
    subset = df[(df["scenario"] == "ubi_only") & (df["post_labor"] == 0.95)]
    grouped = subset.groupby("collectivism_index").agg(
        social_distress=("sink_index", "mean"),
        social_distress_sem=("sink_index", "sem"),
        collapse_probability=("sink_collapsed", "mean"),
        collapse_probability_sem=("sink_collapsed", "sem"),
    )

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    axes[0].plot(grouped.index, grouped["social_distress"], color="#2b6cb0", marker="o", linewidth=2.2)
    axes[0].fill_between(
        grouped.index,
        grouped["social_distress"] - 1.96 * grouped["social_distress_sem"],
        grouped["social_distress"] + 1.96 * grouped["social_distress_sem"],
        color="#2b6cb0",
        alpha=0.16,
    )
    axes[0].set_title("Mean social distress")
    axes[0].set_xlabel("Collectivism index")
    axes[0].set_ylim(0, 1.02)

    axes[1].plot(grouped.index, grouped["collapse_probability"], color="#8c2d04", marker="s", linewidth=2.2)
    axes[1].fill_between(
        grouped.index,
        np.clip(grouped["collapse_probability"] - 1.96 * grouped["collapse_probability_sem"], 0, 1),
        np.clip(grouped["collapse_probability"] + 1.96 * grouped["collapse_probability_sem"], 0, 1),
        color="#8c2d04",
        alpha=0.14,
    )
    axes[1].set_title("Collapse probability")
    axes[1].set_xlabel("Collectivism index")
    axes[1].set_ylim(0, 1.02)

    plt.tight_layout()
    save_figure(MANUSCRIPT_FIGURES[5])


def generate_figure_6() -> None:
    df = pd.read_csv(REPO_ROOT / "data" / "simulation" / "speed_clean_comparison.csv")
    baseline = df[df["scenario"] == "baseline"]
    grouped = (
        baseline.groupby(["speed", "steps_after_target"])
        .agg(
            social_distress=("sink_index", "mean"),
            social_distress_sem=("sink_index", "sem"),
        )
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    for speed, color, marker in [("rapid", "#ba3c2f", "s"), ("gradual", "#2b6cb0", "o")]:
        subset = grouped[grouped["speed"] == speed]
        ax.plot(
            subset["steps_after_target"],
            subset["social_distress"],
            color=color,
            marker=marker,
            linewidth=2.2,
            label=speed.capitalize(),
        )
        ax.fill_between(
            subset["steps_after_target"],
            subset["social_distress"] - 1.96 * subset["social_distress_sem"],
            subset["social_distress"] + 1.96 * subset["social_distress_sem"],
            color=color,
            alpha=0.14,
        )
    ax.set_xlabel("Steps after target displacement is reached")
    ax.set_ylabel("Mean social distress")
    ax.set_ylim(0, 1.0)
    ax.set_title("Exposure-time-controlled automation speed comparison")
    ax.legend()
    save_figure(MANUSCRIPT_FIGURES[6])


def generate_figure_7() -> None:
    df = pd.read_csv(REPO_ROOT / "data" / "simulation" / "sweep6_full_grid.csv")
    scenario_labels = {
        "baseline": "Baseline",
        "fairness": "Fairness",
        "fairness+collectivism": "Fairness + collectivism",
        "ubi_only": "Income support only",
        "UBI+collectivism": "Income support + collectivism",
        "roles": "Roles only",
        "UBI+virtual": "Income support + virtual worlds",
        "roles+virtual": "Roles + virtual worlds",
        "full_bundle": "Full bundle",
        "all_bundle": "All bundle",
    }
    subset = df[df["post_labor"] == 0.95]
    grouped = (
        subset.groupby("scenario")
        .agg(
            social_distress=("sink_index", "mean"),
            social_distress_sem=("sink_index", "sem"),
        )
        .sort_values("social_distress", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(7.8, 5.2))
    y = np.arange(len(grouped))
    ax.barh(y, grouped["social_distress"], color="#2b6cb0", alpha=0.88)
    ax.errorbar(
        grouped["social_distress"],
        y,
        xerr=1.96 * grouped["social_distress_sem"],
        fmt="none",
        ecolor="#1a1a1a",
        elinewidth=0.9,
        capsize=2,
    )
    ax.set_yticks(y)
    ax.set_yticklabels([scenario_labels.get(name, name) for name in grouped.index])
    ax.set_xlabel("Mean social distress")
    ax.set_title("Full-grid bundled scenario ranking at 95% displacement")
    ax.invert_yaxis()
    save_figure(MANUSCRIPT_FIGURES[7])


def generate_figure_8() -> None:
    df = pd.read_csv(REPO_ROOT / "data" / "simulation" / "sweep5_archetypes.csv")
    archetype_columns = [
        ("productive_frac", "Productive", "#4c9a2a"),
        ("beautiful_one_frac", "Beautiful ones", "#d9a404"),
        ("withdrawn_frac", "Withdrawn", "#d97706"),
        ("collapsed_frac", "Collapsed", "#b91c1c"),
        ("aggressor_frac", "Aggressor", "#7c3aed"),
    ]
    fig, axes = plt.subplots(2, 1, figsize=(8.2, 7.6), sharex=True)

    for ax, scenario, title in [
        (axes[0], "baseline", "Baseline"),
        (axes[1], "full_bundle", "Full intervention bundle"),
    ]:
        subset = df[df["scenario"] == scenario]
        means = subset.groupby("step")[[column for column, _, _ in archetype_columns]].mean()
        ax.stackplot(
            means.index,
            [means[column] for column, _, _ in archetype_columns],
            labels=[label for _, label, _ in archetype_columns],
            colors=[color for _, _, color in archetype_columns],
            alpha=0.88,
        )
        ax.set_ylim(0, 1)
        ax.set_ylabel("Population fraction")
        ax.set_title(title)

    axes[1].set_xlabel("Time step")
    axes[0].legend(loc="center left", bbox_to_anchor=(1.01, 0.5))
    plt.tight_layout()
    save_figure(MANUSCRIPT_FIGURES[8])


def generate_manuscript_figures() -> None:
    configure_plotting()
    generate_figure_1()
    generate_figure_2()
    generate_figure_3()
    generate_figure_4()
    generate_figure_5()
    generate_figure_6()
    generate_figure_7()
    generate_figure_8()


def extract_figure_captions(text: str) -> dict[int, str]:
    if "## Appendix: Figures" not in text:
        raise ValueError("Expected '## Appendix: Figures' section in manuscript draft.")
    appendix = text.split("## Appendix: Figures", 1)[1]
    captions: dict[int, str] = {}
    pattern = re.compile(r"\*\*Figure (\d+)\.\*\*\s*(.+?)(?=\n\n\*\*Figure \d+\.\*\*|\Z)", re.S)
    for match in pattern.finditer(appendix):
        number = int(match.group(1))
        captions[number] = " ".join(match.group(2).strip().split())
    missing = [number for number in range(1, 9) if number not in captions]
    if missing:
        raise ValueError(f"Missing figure captions for figure(s): {missing}")
    return captions


def strip_appendix_figures(text: str) -> str:
    return text.split("## Appendix: Figures", 1)[0].rstrip() + "\n"


def inline_markdown(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def block_to_html(block: str, section_context: str | None) -> str:
    if block.startswith("# "):
        return f'<h1 class="paper-title">{inline_markdown(block[2:].strip())}</h1>'
    if block.startswith("## "):
        heading = block[3:].strip()
        return f"<h2>{inline_markdown(heading)}</h2>"
    if block.startswith("### "):
        heading = block[4:].strip()
        return f"<h3>{inline_markdown(heading)}</h3>"
    if block.strip() == "---":
        return '<hr class="section-rule" />'

    paragraph = " ".join(line.strip() for line in block.splitlines())
    css_class = ""
    if section_context == "Abstract":
        css_class = ' class="abstract-paragraph"'
    elif section_context == "References":
        css_class = ' class="reference-item"'
    elif paragraph.startswith("**Anonymous Authors**"):
        css_class = ' class="authors"'
    elif paragraph.startswith("**Keywords:**"):
        css_class = ' class="keywords"'
    return f"<p{css_class}>{inline_markdown(paragraph)}</p>"


def render_figure_html(number: int, caption: str) -> str:
    return (
        '<figure class="paper-figure">'
        f'<img src="{manuscript_figure_path(number)}" alt="Figure {number}" />'
        f"<figcaption><strong>Figure {number}.</strong> {inline_markdown(caption)}</figcaption>"
        "</figure>"
    )


def render_html_document() -> str:
    source_text = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    captions = extract_figure_captions(source_text)
    main_text = strip_appendix_figures(source_text)

    blocks = []
    current: list[str] = []
    for line in main_text.splitlines():
        if not line.strip():
            if current:
                blocks.append("\n".join(current))
                current = []
            continue
        current.append(line.rstrip())
    if current:
        blocks.append("\n".join(current))

    body_parts: list[str] = []
    current_h2: str | None = None
    current_section_number: str | None = None

    def append_figures_for_current_section() -> None:
        if not current_section_number:
            return
        for figure_number in FIGURES_BY_SECTION.get(current_section_number, []):
            body_parts.append(render_figure_html(figure_number, captions[figure_number]))

    for block in blocks:
        if block.startswith("## "):
            append_figures_for_current_section()
            current_section_number = None
            current_h2 = block[3:].strip()
            body_parts.append(block_to_html(block, current_h2))
            continue

        if block.startswith("### "):
            append_figures_for_current_section()
            heading = block[4:].strip()
            match = re.match(r"(\d+\.\d+)", heading)
            current_section_number = match.group(1) if match else None
            body_parts.append(block_to_html(block, current_h2))
            continue

        body_parts.append(block_to_html(block, current_h2))

    append_figures_for_current_section()

    css_href = CSS_PATH.relative_to(REPO_ROOT).as_posix()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Paper 1 JASSS Submission Package</title>
  <link rel="stylesheet" href="../{css_href}" />
</head>
<body>
  <main class="paper-shell">
    {''.join(body_parts)}
  </main>
</body>
</html>
"""


def main() -> None:
    generate_manuscript_figures()
    html_document = render_html_document()
    HTML_OUTPUT_PATH.write_text(html_document, encoding="utf-8")
    print(f"Wrote HTML package to {HTML_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
