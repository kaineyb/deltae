import math

import pytest
from hypothesis import given
from hypothesis import strategies as st

import deltae

# Reference values below were independently computed from the CIE94 formula
# (not by calling deltae.delta_e_94), cross-checked against two independent
# sources that agree exactly:
# - Lindbloom, http://www.brucelindbloom.com/Eqn_DeltaE_CIE94.html
# - Wikipedia, https://en.wikipedia.org/wiki/Color_difference#CIE94

LAB1 = {"L": 50.0, "a": 2.6772, "b": -79.7751}
LAB2 = {"L": 50.0, "a": 0.0, "b": -82.7485}


def test_graphic_arts_default():
    assert round(deltae.delta_e_94(LAB1, LAB2), 4) == 1.395


def test_textiles():
    assert round(deltae.delta_e_94(LAB1, LAB2, application="textiles"), 4) == 1.423


def test_reference_and_sample_are_not_interchangeable():
    """CIE94 weights sC/sH by the reference color's chroma, not an average of
    both colors, so swapping which Lab is the reference changes the result."""
    assert round(deltae.delta_e_94(LAB2, LAB1), 4) == 1.3653
    assert deltae.delta_e_94(LAB1, LAB2) != deltae.delta_e_94(LAB2, LAB1)


def test_asymmetry_can_be_large():
    """A pair with a large chroma gap makes the asymmetry obvious: treating
    the saturated color as reference weights sC/sH much more heavily than
    treating the neutral color as reference."""
    LabSaturated = {"L": 50.0, "a": 20.0, "b": 0.0}
    LabNeutral = {"L": 50.0, "a": 0.0, "b": 0.0}

    assert round(deltae.delta_e_94(LabSaturated, LabNeutral), 4) == 10.5263
    assert round(deltae.delta_e_94(LabNeutral, LabSaturated), 4) == 20.0


l_component = st.floats(min_value=-100, max_value=200, allow_nan=False)
ab_component = st.floats(min_value=-200, max_value=200, allow_nan=False)


@st.composite
def lab(draw):
    return {
        "L": draw(l_component),
        "a": draw(ab_component),
        "b": draw(ab_component),
    }


@given(lab())
def test_identity(Lab):
    assert deltae.delta_e_94(Lab, Lab) == pytest.approx(0.0, abs=1e-9)


@given(lab(), lab())
def test_non_negative(Lab1, Lab2):
    assert deltae.delta_e_94(Lab1, Lab2) >= 0


@st.composite
def equal_chroma_lab_pair(draw):
    """Two Lab dicts guaranteed to share the same chroma, by construction:
    same L for both, a/b placed on the same circle of radius r at different
    angles."""
    L1 = draw(l_component)
    L2 = draw(l_component)
    r = draw(st.floats(min_value=0, max_value=200, allow_nan=False))
    theta1 = draw(st.floats(min_value=0, max_value=2 * math.pi, allow_nan=False))
    theta2 = draw(st.floats(min_value=0, max_value=2 * math.pi, allow_nan=False))

    Lab1 = {"L": L1, "a": r * math.cos(theta1), "b": r * math.sin(theta1)}
    Lab2 = {"L": L2, "a": r * math.cos(theta2), "b": r * math.sin(theta2)}
    return Lab1, Lab2


@given(equal_chroma_lab_pair())
def test_matches_when_chroma_is_equal(pair):
    """sC/sH only depend on which color is the reference through c1's
    chroma, so when both colors have equal chroma, order stops mattering."""
    Lab1, Lab2 = pair
    assert deltae.delta_e_94(Lab1, Lab2) == pytest.approx(
        deltae.delta_e_94(Lab2, Lab1), abs=1e-6
    )
