"""Shared fixtures: a fake token provider and a mocked SDM HTTP layer.

respx intercepts httpx at the transport level, so tests exercise the real
``SDMClient`` request code without touching the network.

Source: https://lundberg.github.io/respx/guide/
"""

from collections.abc import AsyncIterator, Iterator

import httpx
import pytest
import respx

from py_nest_controller.client.sdm import SDMClient

FAKE_ACCESS_TOKEN = "fake-access-token"
"""Bearer token the fake provider hands out."""

FAKE_PROJECT_ID = "00000000-0000-4000-8000-000000000000"
"""A valid UUID shaped Device Access project ID."""

FAKE_DEVICE_ID = "fake-device-id"
"""Bare device ID used across tests."""


class FakeTokenProvider:
    """``TokenProvider`` that returns a fixed token and counts calls.

    Structurally satisfies ``py_nest_controller.auth.TokenProvider``.
    """

    token: str
    calls: int

    def __init__(self, token: str = FAKE_ACCESS_TOKEN) -> None:
        """Store the token and reset the call counter.

        Args:
            token: Token to return from ``get_access_token``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Set ``self.token = token`` and ``self.calls = 0``.
        """
        raise NotImplementedError("To be implemented by developer")

    async def get_access_token(self) -> str:
        """Return the fixed token.

        Returns:
            ``self.token``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Increment ``self.calls``.
            2. Return ``self.token``.
        """
        raise NotImplementedError("To be implemented by developer")


@pytest.fixture
def fake_token_provider() -> FakeTokenProvider:
    """Provide a fresh ``FakeTokenProvider``.

    Returns:
        A new provider with zero calls.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Return ``FakeTokenProvider()``.
    """
    raise NotImplementedError("To be implemented by developer")


@pytest.fixture
def sdm_api_mock() -> Iterator[respx.MockRouter]:
    """Mock every request to the SDM base URL.

    Yields:
        A respx router scoped to ``SDM_API_BASE_URL``. Unmatched requests fail.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. ``with respx.mock(base_url=SDM_API_BASE_URL, assert_all_called=False) as router:``
        2. ``yield router``.
        Docs: https://lundberg.github.io/respx/api/#mock
    """
    raise NotImplementedError("To be implemented by developer")


@pytest.fixture
async def http_client(sdm_api_mock: respx.MockRouter) -> AsyncIterator[httpx.AsyncClient]:
    """Provide an ``httpx.AsyncClient`` whose traffic is routed to the respx mock.

    Args:
        sdm_api_mock: Active router; requesting it ensures mocking is on.

    Yields:
        An open ``AsyncClient``, closed after the test.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. ``async with httpx.AsyncClient() as client: yield client``.
    """
    raise NotImplementedError("To be implemented by developer")


@pytest.fixture
def sdm_client(
    fake_token_provider: FakeTokenProvider,
    http_client: httpx.AsyncClient,
) -> SDMClient:
    """Provide an ``SDMClient`` wired to the fake token provider and mocked HTTP.

    Args:
        fake_token_provider: Supplies the bearer token.
        http_client: Mocked transport.

    Returns:
        A client that does not own ``http_client``.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Build ``SDMClient(device_access_project_id=FAKE_PROJECT_ID, ...)``.
    """
    raise NotImplementedError("To be implemented by developer")


@pytest.fixture
def thermostat_device_json() -> dict[str, object]:
    """Provide a realistic devices.get body for a Nest Thermostat E in HEAT mode.

    Returns:
        A JSON compatible dict with all thermostat traits including Fan.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Copy the sample from the thermostat guide and set mode HEAT.
        Docs: https://developers.google.com/nest/device-access/api/thermostat
    """
    raise NotImplementedError("To be implemented by developer")
