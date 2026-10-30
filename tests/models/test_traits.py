"""Tests for py_nest_controller.models.traits."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_device_traits_parse_full_thermostat(thermostat_device_json: dict[str, object]) -> None:
    """A full thermostat payload parses every trait by its full SDM key."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_present_lists_only_returned_traits(thermostat_device_json: dict[str, object]) -> None:
    """``present()`` returns exactly the trait names found in the payload."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_missing_fan_trait_is_none(thermostat_device_json: dict[str, object]) -> None:
    """Without the Fan trait, ``traits.fan`` is ``None`` and absent from ``present()``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_unknown_traits_are_ignored() -> None:
    """A trait key the SDK does not know does not fail parsing."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_setpoint_trait_allows_missing_values() -> None:
    """The setpoint trait parses when only one or neither setpoint is present."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_humidity_out_of_range_is_rejected() -> None:
    """Humidity above 100 percent fails validation."""
    raise NotImplementedError("To be implemented by developer")
