"""
Stack Exchange data acquisition — scaffold.

Goal: get the public Stack Exchange dump tables we need for so_sdt_study,
starting SMALL (a medium SE site) to debug the pipeline before touching the
~100GB+ full Stack Overflow dump.

Three viable acquisition routes (see DESIGN.md §3):
  1. archive.org community dump (2025-12-31): per-site 7z of XML.
  2. communitydatadump.com: alternative formats (parquet/sqlite) — easier.
  3. BigQuery `bigquery-public-data.stackoverflow`: query without downloading
     100GB+ locally. Best for the exploratory signal check.

This file is a SCAFFOLD: it documents the plan and provides a working
small-site downloader + XML->parquet converter stub. Fill in TODOs as we go.

Usage (intended):
    python download_data.py --site <name> --out ../data/<name>
"""
from __future__ import annotations

import argparse
import os
import sys

# ---- Configuration -----------------------------------------------------------

# Start the pipeline on a SMALL/MEDIUM site, NOT stackoverflow.com.
# Recommended debug site: something tech-adjacent but small enough to iterate.
# (e.g. "datascience", "ai", "softwareengineering" — pick in DESIGN review.)
DEFAULT_DEBUG_SITE = "datascience.stackexchange.com"

# Tables we actually need (see DESIGN.md §3).
NEEDED_TABLES = ["Users", "Posts", "Comments", "Votes", "Badges", "PostHistory", "Tags"]

# archive.org item that hosts the community dump.
ARCHIVE_ITEM = "stackexchange_20251231"


# ---- Route 1: archive.org per-site 7z ----------------------------------------

def download_site_archive(site: str, out_dir: str) -> None:
    """Download a single site's 7z bundle from the archive.org community dump.

    NOTE: archive.org returned HTTP 403 to a generic fetcher during scoping;
    use a real HTTP client with a normal User-Agent, or the `internetarchive`
    Python package (`ia download <item> --glob='<site>*'`).

    TODO:
      - confirm exact filename pattern for `site` in item `ARCHIVE_ITEM`
      - stream-download with requests + tqdm
      - verify checksum
    """
    os.makedirs(out_dir, exist_ok=True)
    raise NotImplementedError(
        "TODO: implement archive.org download. Quick manual path:\n"
        f"  pip install internetarchive\n"
        f"  ia download {ARCHIVE_ITEM} --glob='{site}*'\n"
        "Then point --out at the extracted folder."
    )


# ---- Route 3: BigQuery (preferred for the exploratory signal check) ----------

BIGQUERY_NOTE = """
For the FIRST exploratory pass (does the motivation x differential-exodus
signal even exist?), BigQuery is the least-friction route — no 100GB download.

  pip install google-cloud-bigquery
  # auth: gcloud auth application-default login

  from google.cloud import bigquery
  client = bigquery.Client()
  # bigquery-public-data.stackoverflow has:
  #   posts_questions, posts_answers, users, comments, votes, badges
  # Example: monthly answer counts before/after 2022-11-30 for a user cohort.

Caution: the public BigQuery SO table snapshot may lag; confirm it includes
data through at least 2024-01 before relying on it for outcomes (DESIGN §3).
"""


# ---- XML -> parquet conversion (for Route 1/2 local dumps) --------------------

def xml_to_parquet(xml_path: str, out_path: str) -> None:
    """Convert a Stack Exchange table XML (row-per-line) to parquet.

    SE dump XMLs are <row .../> elements with attributes. Stream with
    lxml.etree.iterparse to avoid loading the whole file into memory
    (Posts can be tens of GB even compressed).

    TODO: implement streaming parse -> pyarrow batches -> parquet.
    """
    raise NotImplementedError("TODO: streaming XML->parquet (lxml iterparse + pyarrow).")


# ---- CLI ---------------------------------------------------------------------

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Acquire Stack Exchange dump tables.")
    ap.add_argument("--site", default=DEFAULT_DEBUG_SITE,
                    help="SE site to download (start small, NOT stackoverflow.com).")
    ap.add_argument("--out", default=None, help="output dir")
    ap.add_argument("--route", choices=["archive", "bigquery", "info"], default="info")
    args = ap.parse_args(argv)

    out = args.out or os.path.join(os.path.dirname(__file__), "..", "data", args.site)

    if args.route == "info":
        print(__doc__)
        print("Needed tables:", ", ".join(NEEDED_TABLES))
        print("\n--- BigQuery route ---")
        print(BIGQUERY_NOTE)
        print(f"Debug site default: {DEFAULT_DEBUG_SITE}")
        print("\nNext: pick debug site in DESIGN review, then implement a download route.")
        return 0
    if args.route == "archive":
        download_site_archive(args.site, out)
        return 0
    if args.route == "bigquery":
        print(BIGQUERY_NOTE)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
