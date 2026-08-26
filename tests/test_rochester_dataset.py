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
    result = deltae._delta_e_2000(
        case["Lab1"], case["Lab2"], test=True, formula="Rochester"
    )

    actual = {
        "a1Prime": result.a1Prime,
        "a2Prime": result.a2Prime,
        "c1Prime": result.c1Prime,
        "c2Prime": result.c2Prime,
        "h1Prime": result.h1Prime,
        "h2Prime": result.h2Prime,
        "hBarPrime": result.hBarPrime,
        "g": result.g,
        "t": result.t,
        "sL": result.sL,
        "sC": result.sC,
        "sH": result.sH,
        "rT": result.rT,
        "de2000": result.DE2000,
    }

    assert actual == case["expected"]


def test_public_api_returns_float_only():
    case = ROCHESTER_DATA[0]

    result = deltae.delta_e_2000(case["Lab1"], case["Lab2"])

    assert isinstance(result, float)
    assert round(result, 4) == case["expected"]["de2000"]


def test_invalid_formula_raises():
    Lab1 = {"L": 50.0, "a": 2.6772, "b": -79.7751}
    Lab2 = {"L": 50.0, "a": 0.0, "b": -82.7485}

    with pytest.raises(ValueError, match="formula"):
        deltae.delta_e_2000(Lab1, Lab2, formula="bogus")
