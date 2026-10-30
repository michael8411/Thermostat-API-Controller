"""Tests for py_nest_controller.auth.store."""

import pytest


@pytest.mark.skip(reason="Not implemented yet")
async def test_empty_store_loads_none() -> None:
    """A new ``InMemoryTokenStore`` returns ``None`` from ``load``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_save_then_load_round_trips() -> None:
    """Saved tokens are returned unchanged by ``load``."""
    raise NotImplementedError("To be implemented by developer")


@pytest.mark.skip(reason="Not implemented yet")
async def test_initial_tokens_are_loaded() -> None:
    """Tokens passed to the constructor are returned by ``load``."""
    raise NotImplementedError("To be implemented by developer")
