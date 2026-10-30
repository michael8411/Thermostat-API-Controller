"""Default in memory ``TokenStore``.

Tokens are lost when the process exits, including the refresh token. Use it
for tests, or for runs seeded from ``NEST_REFRESH_TOKEN``. For real use, swap in
a persistent ``TokenStore`` (for example keyring) so the refresh token survives.
"""

from py_nest_controller.auth.protocols import TokenStore
from py_nest_controller.models.oauth import OAuthTokens


class InMemoryTokenStore(TokenStore):
    """Keeps the latest ``OAuthTokens`` in a private attribute."""

    _tokens: OAuthTokens | None

    def __init__(self, initial: OAuthTokens | None = None) -> None:
        """Create the store, optionally seeded with tokens.

        Args:
            initial: Tokens to start with, or ``None`` for an empty store.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Assign ``initial`` to ``self._tokens``.
        """
        raise NotImplementedError("To be implemented by developer")

    async def load(self) -> OAuthTokens | None:
        """Return the stored tokens.

        Returns:
            The current ``OAuthTokens`` or ``None``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Return ``self._tokens``.
        """
        raise NotImplementedError("To be implemented by developer")

    async def save(self, tokens: OAuthTokens) -> None:
        """Replace the stored tokens.

        Args:
            tokens: The tokens to keep.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Assign ``tokens`` to ``self._tokens``.
        """
        raise NotImplementedError("To be implemented by developer")
