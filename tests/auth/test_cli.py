"""Tests for py_nest_controller.auth.cli."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_url_command_prints_authorization_url(capsys: pytest.CaptureFixture[str]) -> None:
    """``nest-auth url`` prints the PCM URL and returns 0."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_exchange_command_prints_refresh_token(capsys: pytest.CaptureFixture[str]) -> None:
    """``nest-auth exchange CODE`` prints the refresh token line for .env."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_missing_configuration_returns_nonzero(capsys: pytest.CaptureFixture[str]) -> None:
    """Missing OAuth settings print a clear error and return a nonzero code."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_unknown_command_exits_with_usage() -> None:
    """An unknown subcommand exits with argparse usage."""
    raise NotImplementedError("To be implemented by developer")
