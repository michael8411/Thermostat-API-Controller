"""Tests for py_nest_controller.auth.onboarding."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_authorization_url_has_required_params() -> None:
    """The PCM URL contains client_id, redirect_uri, scope, offline access and consent."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_authorization_url_uses_device_access_project_id() -> None:
    """The project ID appears in the partnerconnections path segment."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_authorization_url_includes_state_when_given() -> None:
    """A ``state`` argument is added to the query string."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_exchange_posts_authorization_code() -> None:
    """The exchange sends ``grant_type=authorization_code`` with the code."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_exchange_returns_refresh_token() -> None:
    """A successful exchange returns a ``TokenResponse`` with a refresh token."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_exchange_error_raises_authentication_error() -> None:
    """An OAuth error body raises ``AuthenticationError``."""
    raise NotImplementedError("To be implemented by developer")
