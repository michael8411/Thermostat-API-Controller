"""Tests for py_nest_controller.exceptions."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_all_errors_subclass_nest_error() -> None:
    """Every public exception can be caught with ``except NestError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_permission_denied_is_authentication_error() -> None:
    """``PermissionDeniedError`` is caught by ``except AuthenticationError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_nest_error_stores_status_fields() -> None:
    """``message``, ``http_status`` and ``rpc_status`` are kept on the instance."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_nest_error_str_is_message() -> None:
    """``str(error)`` returns the human readable message."""
    raise NotImplementedError("To be implemented by developer")
