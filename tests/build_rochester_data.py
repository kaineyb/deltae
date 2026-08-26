"""
Converts the Rochester CIEDE2000 whitepaper dataset into tests/data/rochester_data.json.

CIEDE2000.xls isn't committed to this repo (it's Rochester's dataset, not ours to
redistribute) - download it from:
https://hajim.rochester.edu/ece/sites/gsharma/ciede2000/dataNprograms/CIEDE2000.xls
and place it at the repo root before running this script.

Requires the "data" dependency group: uv run --group data python tests/build_rochester_data.py
"""

import json
from pathlib import Path

import pandas as pd

XLS_PATH = Path(__file__).parent.parent / "CIEDE2000.xls"
OUTPUT_PATH = Path(__file__).parent / "data" / "rochester_data.json"

EXPECTED_COLUMNS = {
    "a1'": "a1Prime",
    "a2'": "a2Prime",
    "C1'": "c1Prime",
    "C2'": "c2Prime",
    "h1'": "h1Prime",
    "h2'": "h2Prime",
    "h'_ave": "hBarPrime",
    "G": "g",
    "T": "t",
    "S_L": "sL",
    "S_C": "sC",
    "S_H": "sH",
    "R_T": "rT",
    "dE2000": "de2000",
}


def build():
    df = pd.read_excel(XLS_PATH, sheet_name="DE2000", header=7)

    records = []
    for i, row in df.iterrows():
        records.append(
            {
                "pair": i + 1,
                "Lab1": {"L": row["L1"], "a": row["a1"], "b": row["b1"]},
                "Lab2": {"L": row["L2"], "a": row["a2"], "b": row["b2"]},
                "expected": {
                    field: round(row[column], 4)
                    for column, field in EXPECTED_COLUMNS.items()
                },
            }
        )

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(records, indent=2) + "\n")
    print(f"Wrote {len(records)} pairs to {OUTPUT_PATH}")


if __name__ == "__main__":
    build()
