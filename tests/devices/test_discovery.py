"""Tests for py_nest_controller.devices.discovery."""

import pytest
import respx

from py_nest_controller.client.sdm import SDMClient


@pytest.mark.skip(reason="Not implemented yet")
async def test_list_thermostats_filters_by_type(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """Only devices of type ``sdm.devices.types.THERMOSTAT`` are returned."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_list_thermostats_empty_account(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """No shared devices returns an empty list."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_list_thermostats_uses_bare_device_ids(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """Each ``Thermostat.device_id`` is the last segment of the resource name."""
    raise NotImplementedError("To be implemented by developer")
