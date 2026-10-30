"""Translate SDM error responses and httpx failures into ``NestError`` subclasses.

Mapping to implement (HTTP status / RPC code -> exception):

- 400 FAILED_PRECONDITION -> ``FailedPreconditionError``
- 400 INVALID_ARGUMENT -> ``InvalidArgumentError``
- 401 UNAUTHENTICATED -> ``AuthenticationError``
- 403 PERMISSION_DENIED -> ``PermissionDeniedError``
- 404 NOT_FOUND -> ``NotFoundError``
- 429 RESOURCE_EXHAUSTED -> ``RateLimitedError``
- 503 UNAVAILABLE -> ``DeviceOfflineError`` for device calls (assumption to
  confirm against real responses), otherwise ``ServerError``
- 500, 504 DEADLINE_EXCEEDED, any other 5xx -> ``ServerError``
- anything unrecognized -> ``ServerError`` (5xx) or ``NestError`` (4xx)

Prefer the RPC ``status`` string over the HTTP code when both are present.

Source: https://developers.google.com/nest/device-access/reference/errors/api
"""

import httpx

from py_nest_controller.exceptions import NestError


def error_from_status(http_status: int, rpc_status: str | None, message: str) -> NestError:
    """Pick and construct the exception for one error response.

    Args:
        http_status: HTTP status code of the response.
        rpc_status: The ``error.status`` RPC code, or ``None`` if absent.
        message: The ``error.message`` text, or a fallback description.

    Returns:
        An instance of the matching ``NestError`` subclass (not raised).

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Look up ``rpc_status`` in the table in this module's docstring.
        2. Fall back to ``http_status`` when ``rpc_status`` is missing or unknown.
        3. Pass ``http_status`` and ``rpc_status`` through to the exception.
        Docs: https://developers.google.com/nest/device-access/reference/errors/api
    """
    raise NotImplementedError("To be implemented by developer")


def raise_for_sdm_error(response: httpx.Response) -> None:
    """Raise the matching ``NestError`` if ``response`` is not a success.

    Args:
        response: A completed httpx response from the SDM API.

    Returns:
        ``None`` when the status is 2xx.

    Raises:
        AuthenticationError: 401.
        PermissionDeniedError: 403.
        NotFoundError: 404.
        InvalidArgumentError: 400 INVALID_ARGUMENT.
        FailedPreconditionError: 400 FAILED_PRECONDITION.
        RateLimitedError: 429.
        DeviceOfflineError: 503 on a device call.
        ServerError: Other 5xx or an unparseable body.
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Return immediately on 2xx.
        2. Try to parse the body into ``ApiErrorResponse``; if it is not JSON or
           not that shape, use the reason phrase as the message.
        3. Raise ``error_from_status(...)`` built from the parsed values.
        4. Never include the request's Authorization header in the message.
        Docs: https://developers.google.com/nest/device-access/reference/errors/api
    """
    raise NotImplementedError("To be implemented by developer")


def wrap_transport_error(exc: httpx.HTTPError) -> NestError:
    """Convert an httpx exception that had no usable response into a ``NestError``.

    Args:
        exc: The httpx error, typically ``httpx.TransportError`` or a timeout.

    Returns:
        A ``NestConnectionError`` for transport failures and timeouts, or
        ``NestError`` for anything else. The caller raises it ``from exc``.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. ``httpx.TimeoutException`` and ``httpx.TransportError`` map to
           ``NestConnectionError``.
        2. Keep the message short and free of URLs with tokens.
    """
    raise NotImplementedError("To be implemented by developer")
