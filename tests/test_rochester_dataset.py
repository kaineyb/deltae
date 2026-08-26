import json
from pathlib import Path

import pytest

import deltae

DATA_PATH = Path(__file__).parent / "data" / "rochester_data.json"
ROCHESTER_DATA = json.loads(DATA_PATH.read_text())


@pytest.mark.parametrize(
    "case",
    ROCHESTER_DATA,
    ids=[f"pair_{case['pair']}" for case in ROCHESTER_DATA],
)
def test_delta_e_2000_rochester_dataset(case):
    (
        a1Prime,
        a2Prime,
        c1Prime,
        c2Prime,
        h1Prime,
        h2Prime,
        hBarPrime,
        g,
        t,
        sL,
        sC,
        sH,
        rT,
        de2000,
    ) = deltae.delta_e_2000(case["Lab1"], case["Lab2"], test=True, formula="Rochester")

    actual = {
        "a1Prime": a1Prime,
        "a2Prime": a2Prime,
        "c1Prime": c1Prime,
        "c2Prime": c2Prime,
        "h1Prime": h1Prime,
        "h2Prime": h2Prime,
        "hBarPrime": hBarPrime,
        "g": g,
        "t": t,
        "sL": sL,
        "sC": sC,
        "sH": sH,
        "rT": rT,
        "de2000": de2000,
    }

    assert actual == case["expected"]
