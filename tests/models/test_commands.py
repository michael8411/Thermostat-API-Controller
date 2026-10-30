"""Tests for py_nest_controller.models.commands."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_set_mode_request_body() -> None:
    """``SetThermostatModeCommand`` serializes to the ThermostatMode.SetMode body."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_set_eco_request_body() -> None:
    """``SetEcoModeCommand`` serializes to the ThermostatEco.SetMode body."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_set_heat_uses_camel_case_param() -> None:
    """``SetHeatCommand`` sends ``heatCelsius``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_set_cool_uses_camel_case_param() -> None:
    """``SetCoolCommand`` sends ``coolCelsius``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_set_range_sends_both_params() -> None:
    """``SetRangeCommand`` sends ``heatCelsius`` and ``coolCelsius``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_set_range_rejects_heat_not_below_cool() -> None:
    """``SetRangeCommand`` with heat >= cool raises a validation error."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_fan_timer_duration_serializes_as_seconds_string() -> None:
    """A 15 minute duration serializes to ``"900s"``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_fan_timer_without_duration_omits_param() -> None:
    """``duration=None`` leaves ``duration`` out of the params."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("seconds", [0, 43201])
def test_fan_timer_duration_out_of_range_is_rejected(seconds: int) -> None:
    """Durations outside 1s to 43200s fail validation."""
    raise NotImplementedError("To be implemented by developer")
