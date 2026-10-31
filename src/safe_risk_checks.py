"""Checks educativos y deterministas; no ejecutan órdenes ni llaman a exchanges."""

from math import isfinite


def validate_risk_inputs(equity: float, risk_fraction: float, stop_distance: float) -> bool:
    """Validate inputs for a hypothetical position-size calculation."""
    values = (equity, risk_fraction, stop_distance)
    if not all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in values):
        return False
    if not all(isfinite(value) for value in values):
        return False
    return equity > 0 and 0 < risk_fraction <= 1 and stop_distance > 0


def hypothetical_risk_budget(equity: float, risk_fraction: float, stop_distance: float) -> float:
    """Return a hypothetical risk budget; does not determine or submit an order."""
    if not validate_risk_inputs(equity, risk_fraction, stop_distance):
        raise ValueError("Invalid risk inputs")
    return equity * risk_fraction


def hypothetical_position_units(equity: float, risk_fraction: float, stop_distance: float) -> float:
    """Illustrative position units from budget / stop distance, not exchange-ready sizing."""
    if not validate_risk_inputs(equity, risk_fraction, stop_distance):
        raise ValueError("Invalid risk inputs")
    return hypothetical_risk_budget(equity, risk_fraction, stop_distance) / stop_distance
