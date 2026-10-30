"""Low level async SDM REST client.

Owns URLs, auth headers, response parsing, and error mapping. Knows nothing
about thermostat rules; that lives in ``devices/``.

Source: https://developers.google.com/nest/device-access/reference/rest
"""

from types import TracebackType
from typing import Any, Self

import httpx

from py_nest_controller.auth.protocols import TokenProvider
from py_nest_controller.config import NestSettings
from py_nest_controller.constants import SDM_API_BASE_URL
from py_nest_controller.models.commands import SdmCommand
from py_nest_controller.models.resources import Device, ExecuteCommandResponse, Structure


class SDMClient:
    """Generic async client for ``enterprises/{device_access_project_id}/...`` resources.

    Dependencies are injected: pass an ``httpx.AsyncClient`` and any
    ``TokenProvider``. The client closes the HTTP client on exit only when it
    created it (``owns_http_client=True``, as ``from_settings`` does).

    Usage::

        async with SDMClient.from_settings(settings) as client:
            devices = await client.list_devices()

    Source: https://developers.google.com/nest/device-access/reference/rest
    """

    _device_access_project_id: str
    _token_provider: TokenProvider
    _http_client: httpx.AsyncClient
    _base_url: str
    _owns_http_client: bool

    def __init__(
        self,
        *,
        device_access_project_id: str,
        token_provider: TokenProvider,
        http_client: httpx.AsyncClient,
        base_url: str = SDM_API_BASE_URL,
        owns_http_client: bool = False,
    ) -> None:
        """Store dependencies. Makes no network calls.

        Args:
            device_access_project_id: Device Access project UUID used in every path.
            token_provider: Source of bearer tokens.
            http_client: Client used for all SDM calls.
            base_url: API root. Override only in tests.
            owns_http_client: Close ``http_client`` in ``aclose()`` when ``True``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Assign every argument to its private attribute.
        """
        raise NotImplementedError("To be implemented by developer")

    @classmethod
    def from_settings(
        cls,
        settings: NestSettings,
        *,
        http_client: httpx.AsyncClient | None = None,
        token_provider: TokenProvider | None = None,
    ) -> Self:
        """Build a ready to use client from settings.

        Args:
            settings: Validated runtime settings.
            http_client: Optional shared client. When ``None`` a new one is
                created and owned by the returned ``SDMClient``.
            token_provider: Optional provider. When ``None`` an
                ``OAuthTokenManager`` is built from settings using the same HTTP client.

        Returns:
            A configured ``SDMClient``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Create an ``httpx.AsyncClient`` with a sensible timeout if none was given.
            2. Build ``OAuthTokenManager.from_settings`` if no provider was given.
            3. Set ``owns_http_client`` to whether you created the HTTP client.
        """
        raise NotImplementedError("To be implemented by developer")

    async def __aenter__(self) -> Self:
        """Enter the async context.

        Returns:
            This client.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Return ``self``. No setup is needed.
        """
        raise NotImplementedError("To be implemented by developer")

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        """Exit the async context and release resources.

        Args:
            exc_type: Exception type raised inside the block, if any.
            exc: Exception instance raised inside the block, if any.
            tb: Traceback of that exception, if any.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Await ``aclose()``. Do not suppress exceptions.
        """
        raise NotImplementedError("To be implemented by developer")

    async def aclose(self) -> None:
        """Close the HTTP client if this instance owns it.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. If ``self._owns_http_client``, await ``self._http_client.aclose()``.
        """
        raise NotImplementedError("To be implemented by developer")

    @property
    def enterprise_name(self) -> str:
        """Resource name of the enterprise: ``enterprises/{device_access_project_id}``.

        Returns:
            The enterprise resource name.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Format ``constants.ENTERPRISE_PATH_TEMPLATE``.
        """
        raise NotImplementedError("To be implemented by developer")

    def device_name(self, device_id: str) -> str:
        """Full resource name for a device: ``enterprises/{project}/devices/{device_id}``.

        Args:
            device_id: Bare device ID.

        Returns:
            The device resource name.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Join ``enterprise_name``, ``devices``, and ``device_id`` with ``/``.
        """
        raise NotImplementedError("To be implemented by developer")

    async def list_devices(self) -> list[Device]:
        """List every device the user shared with this project.

        Returns:
            Parsed devices. Empty if none were shared.

        Raises:
            AuthenticationError: Token rejected.
            PermissionDeniedError: Access not granted.
            NotFoundError: Wrong Device Access project ID ("Enterprise not found.").
            RateLimitedError: More than 5 list calls per minute (Sandbox).
            ServerError: 5xx.
            NestConnectionError: Network failure.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. GET ``{enterprise_name}/devices`` through ``_request``.
            2. Parse with ``ListDevicesResponse`` and return its devices as a list.
            Docs: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/list
        """
        raise NotImplementedError("To be implemented by developer")

    async def get_device(self, device_id: str) -> Device:
        """Fetch one device with all of its current traits.

        Args:
            device_id: Bare device ID.

        Returns:
            The parsed device.

        Raises:
            NotFoundError: No such device.
            RateLimitedError: More than 10 get calls per minute (Sandbox).
            AuthenticationError: Token rejected.
            ServerError: 5xx.
            NestConnectionError: Network failure.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. GET ``device_name(device_id)`` through ``_request``.
            2. Parse with ``Device``.
            Docs: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/get
        """
        raise NotImplementedError("To be implemented by developer")

    async def list_structures(self) -> list[Structure]:
        """List the structures (homes) the user shared.

        Returns:
            Parsed structures.

        Raises:
            AuthenticationError: Token rejected.
            NotFoundError: Wrong Device Access project ID.
            RateLimitedError: Quota exceeded.
            ServerError: 5xx.
            NestConnectionError: Network failure.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. GET ``{enterprise_name}/structures`` through ``_request``.
            2. Parse with ``ListStructuresResponse``.
            Docs: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.structures/list
        """
        raise NotImplementedError("To be implemented by developer")

    async def execute_command(self, device_id: str, command: SdmCommand) -> ExecuteCommandResponse:
        """Send one command to a device.

        Args:
            device_id: Bare device ID.
            command: Any ``SdmCommand`` subclass instance.

        Returns:
            The parsed command response. Thermostat commands return empty results.

        Raises:
            FailedPreconditionError: Device state does not allow the command.
            InvalidArgumentError: Bad params, for example heat >= cool in SetRange.
            RateLimitedError: More than 5 commands per minute for this device.
            DeviceOfflineError: Device unreachable.
            NotFoundError: No such device.
            AuthenticationError: Token rejected.
            ServerError: 5xx.
            NestConnectionError: Network failure.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. POST ``{device_name(device_id)}:executeCommand`` (note the colon,
               not a slash) through ``_request``.
            2. Body is ``command.to_request_body()`` dumped by alias.
            3. Do not retry automatically on RESOURCE_EXHAUSTED; let the caller decide.
            Docs: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/executeCommand
        """
        raise NotImplementedError("To be implemented by developer")

    async def _request(
        self,
        method: str,
        path: str,
        *,
        json_body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Send one authenticated request and return the decoded JSON body.

        Args:
            method: HTTP method, ``"GET"`` or ``"POST"``.
            path: Resource path relative to ``base_url``, without a leading slash.
            json_body: JSON body for POST, or ``None``.

        Returns:
            The decoded JSON object, or an empty dict for an empty body.

        Raises:
            NestError: Any subclass from ``raise_for_sdm_error`` or ``wrap_transport_error``.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Get a token from ``self._token_provider.get_access_token()``.
            2. Send with ``Authorization: Bearer <token>`` and JSON content type.
            3. On ``httpx.HTTPError`` raise ``wrap_transport_error(exc) from exc``.
            4. On 401, optionally force one token refresh and retry once.
            5. Call ``raise_for_sdm_error(response)`` then decode JSON.
            6. Never log the token or the full headers.
            Docs: https://developers.google.com/nest/device-access/reference/errors/api
        """
        raise NotImplementedError("To be implemented by developer")
