"""Protocols that decouple token consumers from token implementations.

``SDMClient`` depends on ``TokenProvider`` only, so tests can pass a fake and
consumers can supply their own source of tokens. ``OAuthTokenManager``
depends on ``TokenStore`` only, so persistence can change without touching it.

Protocol members are declarations and use ``...`` as their body.
"""

from typing import Protocol, runtime_checkable

from py_nest_controller.models.oauth import OAuthTokens


@runtime_checkable
class TokenProvider(Protocol):
    """Anything that can hand out a currently valid SDM access token."""

    async def get_access_token(self) -> str:
        """Return a bearer token that is valid for at least the next few minutes.

        Returns:
            The raw access token string, ready for an ``Authorization: Bearer`` header.

        Raises:
            AuthenticationError: A token could not be obtained.
            NestConnectionError: The token endpoint was unreachable.
        """
        ...


@runtime_checkable
class TokenStore(Protocol):
    """Persistence for the OAuth token set."""

    async def load(self) -> OAuthTokens | None:
        """Return the stored tokens, or ``None`` if nothing has been saved yet.

        Returns:
            The last saved ``OAuthTokens`` or ``None``.
        """
        ...

    async def save(self, tokens: OAuthTokens) -> None:
        """Persist a token set, replacing any previous one.

        Args:
            tokens: The tokens to store.
        """
        ...
