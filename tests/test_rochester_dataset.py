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


def test_invalid_formula_raises():
    Lab1 = {"L": 50.0, "a": 2.6772, "b": -79.7751}
    Lab2 = {"L": 50.0, "a": 0.0, "b": -82.7485}

    with pytest.raises(ValueError, match="formula"):
        deltae.delta_e_2000(Lab1, Lab2, formula="bogus")
