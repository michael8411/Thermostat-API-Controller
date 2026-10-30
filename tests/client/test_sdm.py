"""Tests for py_nest_controller.client.sdm."""

import pytest
import respx

from py_nest_controller.client.sdm import SDMClient
from tests.conftest import FakeTokenProvider


@pytest.mark.skip(reason="Not implemented yet")
def test_enterprise_name(sdm_client: SDMClient) -> None:
    """``enterprise_name`` is ``enterprises/<project id>``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_requests_send_bearer_token(
    sdm_client: SDMClient,
    sdm_api_mock: respx.MockRouter,
    fake_token_provider: FakeTokenProvider,
) -> None:
    """Every request carries ``Authorization: Bearer <token>`` from the provider."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_list_devices_parses_devices(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``list_devices`` returns parsed ``Device`` models."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_list_devices_empty_body(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """An empty ``{}`` body returns an empty list."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_get_device_uses_full_resource_name(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``get_device`` requests ``enterprises/<project>/devices/<id>``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_list_structures(sdm_client: SDMClient, sdm_api_mock: respx.MockRouter) -> None:
    """``list_structures`` returns parsed ``Structure`` models."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_execute_command_posts_command_body(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """``execute_command`` POSTs ``{"command": ..., "params": ...}`` to ``:executeCommand``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_rate_limited_raises_rate_limited_error(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """A 429 RESOURCE_EXHAUSTED response raises ``RateLimitedError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_rate_limited_is_not_retried(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """A 429 is surfaced after one request; the client does not hammer the quota."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_http_error_is_mapped(sdm_client: SDMClient, sdm_api_mock: respx.MockRouter) -> None:
    """A 404 response raises ``NotFoundError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_transport_error_is_wrapped(
    sdm_client: SDMClient, sdm_api_mock: respx.MockRouter
) -> None:
    """A connection failure raises ``NestConnectionError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_owned_http_client_is_closed(fake_token_provider: FakeTokenProvider) -> None:
    """With ``owns_http_client=True``, leaving ``async with`` closes the HTTP client."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_borrowed_http_client_is_left_open(
    sdm_client: SDMClient, fake_token_provider: FakeTokenProvider
) -> None:
    """With ``owns_http_client=False``, ``aclose`` leaves the HTTP client open."""
    raise NotImplementedError("To be implemented by developer")
