import math

import pytest
from hypothesis import given
from hypothesis import strategies as st

import deltae

l_component = st.floats(min_value=-100, max_value=200, allow_nan=False)
ab_component = st.floats(min_value=-200, max_value=200, allow_nan=False)


@st.composite
def lab(draw):
    return {
        "L": draw(l_component),
        "a": draw(ab_component),
        "b": draw(ab_component),
    }


def euclidean(Lab1, Lab2):
    return math.dist(
        (Lab1["L"], Lab1["a"], Lab1["b"]), (Lab2["L"], Lab2["a"], Lab2["b"])
    )


@given(lab(), lab())
def test_matches_euclidean_distance(Lab1, Lab2):
    """delta_e_1976 is, by definition, Euclidean distance in Lab space."""
    assert deltae.delta_e_1976(Lab1, Lab2) == pytest.approx(euclidean(Lab1, Lab2))


@given(lab())
def test_identity(Lab):
    assert deltae.delta_e_1976(Lab, Lab) == 0


@given(lab(), lab())
def test_non_negative(Lab1, Lab2):
    assert deltae.delta_e_1976(Lab1, Lab2) >= 0


@given(lab(), lab())
def test_symmetric(Lab1, Lab2):
    assert deltae.delta_e_1976(Lab1, Lab2) == deltae.delta_e_1976(Lab2, Lab1)


@given(lab(), lab(), lab())
def test_triangle_inequality(Lab1, Lab2, Lab3):
    direct = deltae.delta_e_1976(Lab1, Lab3)
    via_midpoint = deltae.delta_e_1976(Lab1, Lab2) + deltae.delta_e_1976(Lab2, Lab3)
    assert direct <= via_midpoint + abs(via_midpoint) * 1e-9 + 1e-9
