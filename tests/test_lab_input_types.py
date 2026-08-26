from dataclasses import FrozenInstanceError

import pytest

import deltae

LAB1_DICT = {"L": 50.0, "a": 2.6772, "b": -79.7751}
LAB2_DICT = {"L": 50.0, "a": 0.0, "b": -82.7485}

LAB1 = deltae.Lab(**LAB1_DICT)
LAB2 = deltae.Lab(**LAB2_DICT)

FUNCTIONS = [deltae.delta_e_1976, deltae.delta_e_94, deltae.delta_e_2000]


@pytest.mark.parametrize("func", FUNCTIONS)
def test_lab_dataclass_matches_dict_input(func):
    assert func(LAB1, LAB2) == func(LAB1_DICT, LAB2_DICT)


@pytest.mark.parametrize("func", FUNCTIONS)
def test_mixed_lab_and_dict_input(func):
    assert func(LAB1, LAB2_DICT) == func(LAB1_DICT, LAB2)


def test_lab_is_frozen():
    with pytest.raises(FrozenInstanceError):
        LAB1.L = 999
