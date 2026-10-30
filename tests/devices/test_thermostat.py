"""Tests for py_nest_controller.devices.thermostat."""

import pytest
import respx

from py_nest_controller.client.sdm import SDMClient


@pytest.mark.skip(reason="Not implemented yet")
async def test_get_state_returns_snapshot(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``get_state`` returns a ``ThermostatState`` built from devices.get."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_supports_uses_cached_device(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """A second ``supports`` call makes no new request unless ``refresh=True``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_set_mode_sends_command(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``set_mode(COOL)`` sends ThermostatMode.SetMode with ``mode=COOL``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_set_mode_rejects_unavailable_mode(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """A mode missing from ``availableModes`` raises ``InvalidArgumentError`` locally."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_set_heat_in_heat_mode_sends_command(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``set_heat`` in HEAT mode sends SetHeat with ``heatCelsius``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_set_heat_in_cool_mode_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``set_heat`` in COOL mode raises ``FailedPreconditionError`` without sending a command."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_set_cool_in_heat_mode_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``set_cool`` in HEAT mode raises ``FailedPreconditionError`` without sending a command."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_set_range_outside_heatcool_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``set_range`` in HEAT mode raises ``FailedPreconditionError`` without sending a command."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_setpoint_in_off_mode_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """Any setpoint command in OFF mode raises ``FailedPreconditionError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_setpoint_in_manual_eco_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """Any setpoint command while Eco is MANUAL_ECO raises ``FailedPreconditionError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_set_range_heat_not_below_cool_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``set_range(22, 20)`` raises ``InvalidArgumentError`` without sending a command."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_server_failed_precondition_is_raised(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """Server FAILED_PRECONDITION after a passing local check raises ``FailedPreconditionError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_set_eco_on_sends_manual_eco(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``set_eco(True)`` sends ThermostatEco.SetMode with ``MANUAL_ECO``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_start_fan_sends_duration(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``start_fan(timedelta(minutes=30))`` sends ``timerMode=ON`` and ``duration="1800s"``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_start_fan_without_fan_trait_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``start_fan`` on a device without the Fan trait raises ``UnsupportedTraitError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_stop_fan_without_fan_trait_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``stop_fan`` on a device without the Fan trait raises ``UnsupportedTraitError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_start_fan_duration_out_of_range_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """A 13 hour duration raises ``InvalidArgumentError`` without sending a command."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_command_rate_limited_raises(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """A 429 on executeCommand raises ``RateLimitedError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_offline_device_raises(sdm_client: SDMClient, sdm_api_mock: respx.MockRouter) -> None:
    """A command to a device with Connectivity OFFLINE raises ``DeviceOfflineError``."""
    raise NotImplementedError("To be implemented by developer")
