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


@pytest.mark.parametrize(
    "equity,fraction,distance",
    [
        (math.nan, 0.01, 1),
        (-math.inf, 0.01, 1),
        (100, math.inf, 1),
        (100, -math.inf, 1),
        (100, 0.01, math.nan),
        (100, 0.01, math.inf),
        ("100", 0.01, 1),
        (100, "0.01", 1),
        (100, 0.01, "1"),
        (None, 0.01, 1),
        (100, None, 1),
        (100, 0.01, None),
        (False, 0.01, 1),
        (100, True, 1),
        (100, 0.01, True),
    ],
)
def test_non_finite_wrong_type_and_boolean_inputs_are_rejected(equity, fraction, distance):
    assert not validate_risk_inputs(equity, fraction, distance)


@pytest.mark.parametrize(
    "equity,fraction,distance",
    [
        (1, 1, 1),
        (1, 0.000001, 0.5),
        (1_000_000, 0.25, 0.01),
    ],
)
def test_valid_boundary_and_extreme_scale_inputs(equity, fraction, distance):
    assert validate_risk_inputs(equity, fraction, distance)
    assert hypothetical_risk_budget(equity, fraction, distance) == equity * fraction
    assert hypothetical_position_units(equity, fraction, distance) == pytest.approx(
        equity * fraction / distance
    )


def test_risk_budget_scales_linearly_with_equity():
    base = hypothetical_risk_budget(1_000, 0.02, 10)
    doubled = hypothetical_risk_budget(2_000, 0.02, 10)
    assert doubled == 2 * base


def test_position_units_decrease_when_stop_distance_increases():
    tight_stop = hypothetical_position_units(1_000, 0.02, 5)
    wide_stop = hypothetical_position_units(1_000, 0.02, 10)
    assert tight_stop == 2 * wide_stop
