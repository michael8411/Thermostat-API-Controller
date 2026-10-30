"""Tests for py_nest_controller.models.state."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_from_device_maps_all_fields(thermostat_device_json: dict[str, object]) -> None:
    """``ThermostatState.from_device`` fills every field from a full payload."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_from_device_eco_active_has_no_setpoints(
    thermostat_device_json: dict[str, object],
) -> None:
    """In MANUAL_ECO, setpoints are ``None`` and ``is_eco_active`` is ``True``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_from_device_without_fan_trait(thermostat_device_json: dict[str, object]) -> None:
    """Without the Fan trait, fan fields are ``None``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_is_online_reflects_connectivity(thermostat_device_json: dict[str, object]) -> None:
    """``is_online`` is ``False`` when Connectivity reports OFFLINE."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_state_is_frozen(thermostat_device_json: dict[str, object]) -> None:
    """Assigning to a ``ThermostatState`` field raises a validation error."""
    raise NotImplementedError("To be implemented by developer")
