"""Tests for py_nest_controller.client.errors."""

import pytest

from py_nest_controller.exceptions import (
    AuthenticationError,
    DeviceOfflineError,
    FailedPreconditionError,
    InvalidArgumentError,
    NestError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
)


@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize(
    ("http_status", "rpc_status", "expected"),
    [
        (400, "INVALID_ARGUMENT", InvalidArgumentError),
        (400, "FAILED_PRECONDITION", FailedPreconditionError),
        (401, "UNAUTHENTICATED", AuthenticationError),
        (403, "PERMISSION_DENIED", PermissionDeniedError),
        (404, "NOT_FOUND", NotFoundError),
        (429, "RESOURCE_EXHAUSTED", RateLimitedError),
        (500, "INTERNAL", ServerError),
        (503, "UNAVAILABLE", DeviceOfflineError),
        (504, "DEADLINE_EXCEEDED", ServerError),
    ],
)
def test_error_from_status_maps_each_code(
    http_status: int, rpc_status: str, expected: type[NestError]
) -> None:
    """Each HTTP and RPC status pair maps to its documented ``NestError`` subclass."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_unknown_4xx_maps_to_nest_error() -> None:
    """An unlisted 4xx falls back to plain ``NestError`` with the status kept."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_raise_for_sdm_error_passes_on_2xx() -> None:
    """A 200 response does not raise."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_raise_for_sdm_error_reads_google_error_body() -> None:
    """The message and RPC status come from the ``error`` object in the body."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_raise_for_sdm_error_handles_non_json_body() -> None:
    """A 502 with an HTML body still raises ``ServerError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_wrap_transport_error_timeout() -> None:
    """An ``httpx.TimeoutException`` becomes ``NestConnectionError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_wrap_transport_error_connect_error() -> None:
    """An ``httpx.ConnectError`` becomes ``NestConnectionError``."""
    raise NotImplementedError("To be implemented by developer")
