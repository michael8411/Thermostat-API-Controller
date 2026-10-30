"""Tests for py_nest_controller.config."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_load_settings_reads_nest_prefixed_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """All ``NEST_`` variables populate ``NestSettings``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_load_settings_missing_refresh_token_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    """A missing ``NEST_REFRESH_TOKEN`` raises ``ConfigurationError`` naming the variable."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_oauth_client_settings_do_not_need_refresh_token(monkeypatch: pytest.MonkeyPatch) -> None:
    """``load_oauth_client_settings`` succeeds before a refresh token exists."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_gcp_project_id_in_device_access_field_is_rejected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A GCP style project ID in ``NEST_DEVICE_ACCESS_PROJECT_ID`` raises ``ConfigurationError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_empty_env_values_are_treated_as_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """An empty optional variable becomes ``None`` instead of an empty string."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
def test_secrets_are_hidden_in_repr(monkeypatch: pytest.MonkeyPatch) -> None:
    """``repr(settings)`` does not contain the client secret or refresh token."""
    raise NotImplementedError("To be implemented by developer")
