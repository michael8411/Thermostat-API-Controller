"""Tests for py_nest_controller.auth.manager."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
async def test_first_call_refreshes() -> None:
    """With an empty store, ``get_access_token`` calls the token endpoint once."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_fresh_token_is_reused() -> None:
    """A token far from expiry is returned without another refresh."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_refreshes_when_within_margin_of_expiry() -> None:
    """A token expiring inside the refresh margin triggers a refresh."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_refreshes_when_expired() -> None:
    """An already expired token triggers a refresh."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_concurrent_calls_refresh_once() -> None:
    """Many concurrent ``get_access_token`` calls cause exactly one token request."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_refreshed_tokens_are_saved_to_store() -> None:
    """A successful refresh writes the new tokens to the ``TokenStore``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_rotated_refresh_token_is_kept() -> None:
    """If Google returns a new refresh token, the manager uses it next time."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_invalid_grant_raises_authentication_error() -> None:
    """An ``invalid_grant`` response raises ``AuthenticationError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_transport_failure_raises_connection_error() -> None:
    """A network error during refresh raises ``NestConnectionError``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_failed_refresh_does_not_poison_lock() -> None:
    """After a failed refresh, the next call can refresh again."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_seed_refresh_token_used_when_store_empty() -> None:
    """With an empty store, the seed refresh token is sent to the token endpoint."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_stored_refresh_token_wins_over_seed() -> None:
    """When the store holds tokens, their refresh token is used, not the seed."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_no_stored_token_and_no_seed_raises_authentication_error() -> None:
    """An empty store and no seed raise ``AuthenticationError`` naming ``nest-auth``."""
    raise NotImplementedError("To be implemented by developer")
