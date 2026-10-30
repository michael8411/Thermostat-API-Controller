"""Exception hierarchy for the SDK.

Every public method in the package raises only ``NestError`` subclasses. Raw
httpx and Pydantic errors must be caught where they happen and re-raised as one
of these, with the original chained using ``raise ... from exc``.

SDM error bodies look like ``{"error": {"code", "message", "status"}}`` where
``code`` is the HTTP status and ``status`` is the RPC code. The mapping from
those to the classes below lives in ``client/errors.py``.

Source: https://developers.google.com/nest/device-access/reference/errors/api
"""


class NestError(Exception):
    """Base class for every error raised by py-nest-controller.

    Attributes:
        message: Human readable description. For API errors, the SDM ``message``.
        http_status: HTTP status code from the response, if the error came from HTTP.
        rpc_status: SDM RPC code such as ``"FAILED_PRECONDITION"``, if present.
    """

    message: str
    http_status: int | None
    rpc_status: str | None

    def __init__(
        self,
        message: str,
        *,
        http_status: int | None = None,
        rpc_status: str | None = None,
    ) -> None:
        """Create the error and store its details.

        Args:
            message: Human readable description of what went wrong.
            http_status: HTTP status code, when the error came from an HTTP response.
            rpc_status: SDM RPC code string, when the response body included one.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Call ``super().__init__(message)`` so ``str(err)`` shows the message.
            2. Store the three values on ``self`` under the attribute names above.
            3. Optionally override ``__repr__`` to include the RPC code for logs.
        """
        raise NotImplementedError("To be implemented by developer")


class ConfigurationError(NestError):
    """Required settings are missing or invalid.

    Raised by ``config.load_settings()`` when pydantic-settings rejects the
    environment. The message should list every missing ``NEST_*`` variable.
    """


class AuthenticationError(NestError):
    """OAuth failed or the API rejected the access token (HTTP 401, UNAUTHENTICATED).

    Also raised when Google's token endpoint returns ``invalid_grant``, which
    usually means the refresh token was revoked or unused for 6 months and the
    one time setup must be repeated.

    Source: https://developers.google.com/nest/device-access/authorize
    """


class PermissionDeniedError(AuthenticationError):
    """The token is valid but lacks access (HTTP 403, PERMISSION_DENIED).

    Common causes: the user did not grant the device in the PCM consent screen,
    or the Device Access project ID does not match the OAuth client.

    Source: https://developers.google.com/nest/device-access/reference/errors/api
    """


class NotFoundError(NestError):
    """Device, structure, or enterprise does not exist (HTTP 404, NOT_FOUND).

    A wrong Device Access project ID shows up as "Enterprise not found."

    Source: https://developers.google.com/nest/device-access/reference/errors/api
    """


class InvalidArgumentError(NestError):
    """The request was malformed (HTTP 400, INVALID_ARGUMENT).

    Example: SetRange with heat not below cool returns "Cool value must be
    greater than heat value."

    Source: https://developers.google.com/nest/device-access/reference/errors/api
    """


class FailedPreconditionError(NestError):
    """The device state does not allow the command (HTTP 400, FAILED_PRECONDITION).

    Documented thermostat causes:
    - Setpoint command does not match the mode (SetHeat needs HEAT, SetCool needs
      COOL, SetRange needs HEATCOOL).
    - Setpoints cannot change while Eco is MANUAL_ECO.
    - Some models cannot change Eco while the mode is OFF.
    - "Thermostat fan unavailable." for fan commands on a system without a fan.

    Source: https://developers.google.com/nest/device-access/api/thermostat
    """


class RateLimitedError(NestError):
    """Quota exceeded (HTTP 429, RESOURCE_EXHAUSTED, message "Rate limited.").

    Sandbox allows 5 commands per minute per device and 100 per hour for
    thermostats. Retry after the quota resets.

    Source: https://developers.google.com/nest/device-access/project/limits
    """


class DeviceOfflineError(NestError):
    """The thermostat is not reachable.

    The error docs list no dedicated offline code. Raise this when the
    Connectivity trait reports OFFLINE before a command, and when the API
    returns HTTP 503 UNAVAILABLE for a device call.

    Source: https://developers.google.com/nest/device-access/traits/device/connectivity
    """


class UnsupportedTraitError(NestError):
    """The device does not expose a trait the operation needs.

    Raised locally, before calling the API, when a trait is absent from the
    device's GET response (for example no Fan trait on a system without a fan).

    Source: https://developers.google.com/nest/device-access/api/thermostat
    """


class ServerError(NestError):
    """Google returned a 5xx response or an unexpected error shape.

    Covers INTERNAL, DEADLINE_EXCEEDED (504), and any status the mapping does
    not recognize. Usually safe to retry with backoff.

    Source: https://developers.google.com/nest/device-access/reference/errors/api
    """


class NestConnectionError(NestError):
    """The HTTP request never got a response (DNS failure, timeout, connection reset).

    Wraps ``httpx.TransportError`` so callers never see httpx exceptions.
    """
