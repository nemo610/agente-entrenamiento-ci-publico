import math
import pytest

from safe_risk_checks import (
    hypothetical_position_units,
    hypothetical_risk_budget,
    validate_risk_inputs,
)


def test_valid_inputs_are_accepted():
    assert validate_risk_inputs(10_000, 0.01, 100)


def test_risk_budget_is_deterministic():
    assert hypothetical_risk_budget(10_000, 0.01, 100) == 100


def test_position_units_are_hypothetical_budget_divided_by_stop_distance():
    assert hypothetical_position_units(10_000, 0.01, 100) == 1


@pytest.mark.parametrize(
    "equity,fraction,distance",
    [
        (0, 0.01, 1),
        (-1, 0.01, 1),
        (100, 0, 1),
        (100, 1.1, 1),
        (100, 0.01, 0),
        (100, 0.01, -1),
        (math.inf, 0.01, 1),
        (100, math.nan, 1),
        (True, 0.01, 1),
    ],
)
def test_invalid_inputs_are_rejected(equity, fraction, distance):
    assert not validate_risk_inputs(equity, fraction, distance)
    with pytest.raises(ValueError):
        hypothetical_risk_budget(equity, fraction, distance)
    with pytest.raises(ValueError):
        hypothetical_position_units(equity, fraction, distance)
