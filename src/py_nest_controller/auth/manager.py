"""Concrete ``TokenProvider`` that refreshes Google OAuth access tokens.

Source: https://developers.google.com/nest/device-access/authorize
"""

import asyncio
from collections.abc import Callable
from datetime import datetime, timedelta

import httpx
from pydantic import SecretStr

from py_nest_controller.auth.protocols import TokenProvider, TokenStore
from py_nest_controller.config import NestSettings
from py_nest_controller.constants import DEFAULT_TOKEN_REFRESH_MARGIN, OAUTH_TOKEN_URL
from py_nest_controller.models.oauth import OAuthTokens


class OAuthTokenManager(TokenProvider):
    """Caches the access token and refreshes it shortly before it expires.

    Behavior to implement:
        - Token ownership: the ``TokenStore`` owns the refresh token. The
          optional seed from the constructor is used only while the store is
          empty, and the first successful refresh writes it into the store.
        - Caching: keep the current ``OAuthTokens`` in the ``TokenStore`` and
          return its access token while it is still fresh.
        - Safety margin: treat a token as stale when ``expires_at - margin`` is
          in the past, so a request never leaves with a token that dies in flight.
        - Single flight: guard refresh with an ``asyncio.Lock``. Concurrent
          callers that find a stale token wait on the lock, then re-check the
          cache after acquiring it, so only the first one calls Google.
        - Injection: the HTTP client, store, and clock are passed in so tests
          can control time and responses.

    Source: https://developers.google.com/nest/device-access/authorize
    """

    _client_id: str
    _client_secret: SecretStr
    _seed_refresh_token: SecretStr | None
    _http_client: httpx.AsyncClient
    _store: TokenStore
    _refresh_margin: timedelta
    _clock: Callable[[], datetime]
    _token_url: str
    _lock: asyncio.Lock

    def __init__(
        self,
        *,
        client_id: str,
        client_secret: SecretStr,
        http_client: httpx.AsyncClient,
        refresh_token: SecretStr | None = None,
        store: TokenStore | None = None,
        refresh_margin: timedelta = DEFAULT_TOKEN_REFRESH_MARGIN,
        clock: Callable[[], datetime] | None = None,
        token_url: str = OAUTH_TOKEN_URL,
    ) -> None:
        """Store dependencies. Makes no network calls.

        Args:
            client_id: OAuth 2.0 client ID.
            client_secret: OAuth 2.0 client secret.
            http_client: Client used for token endpoint calls. Not closed by this class.
            refresh_token: Optional seed, used only when ``store.load()`` returns
                ``None``. Normally ``nest-auth exchange`` has already saved the
                refresh token to the store and this is left as ``None``.
            store: Where tokens are cached. Defaults to ``InMemoryTokenStore``.
            refresh_margin: How long before expiry a token counts as stale.
            clock: Returns the current timezone aware UTC time. Defaults to
                ``datetime.now(UTC)``. Inject a fake in tests.
            token_url: Token endpoint. Override only in tests.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Assign every argument to its private attribute
               (``refresh_token`` goes to ``self._seed_refresh_token``).
            2. Default ``store`` to a new ``InMemoryTokenStore`` and ``clock`` to
               a UTC ``now`` function.
            3. Create ``self._lock = asyncio.Lock()``.
        """
        raise NotImplementedError("To be implemented by developer")

    @classmethod
    def from_settings(
        cls,
        settings: NestSettings,
        *,
        http_client: httpx.AsyncClient,
        store: TokenStore | None = None,
    ) -> "OAuthTokenManager":
        """Build a manager from loaded settings.

        Args:
            settings: Validated runtime settings.
            http_client: Client used for token endpoint calls.
            store: Optional token store. Defaults to in memory.

        Returns:
            A configured ``OAuthTokenManager``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Pass ``oauth_client_id`` and ``oauth_client_secret`` from settings
               into the constructor.
            2. Pass ``settings.refresh_token`` (often ``None``) as the seed.
        """
        raise NotImplementedError("To be implemented by developer")

    async def get_access_token(self) -> str:
        """Return a fresh access token, refreshing if needed.

        Returns:
            The raw bearer token string.

        Raises:
            AuthenticationError: No refresh token is stored or seeded, or Google
                rejected it (``invalid_grant``).
            NestConnectionError: The token endpoint was unreachable.
            ServerError: The token endpoint returned 5xx.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Load tokens from the store. If present and not stale, return them.
            2. Otherwise acquire ``self._lock``.
            3. Inside the lock, load again: another caller may have refreshed.
            4. If still stale, call ``refresh()`` and return the new token.
            5. Use ``get_secret_value()`` only at the moment you return the string.
        """
        raise NotImplementedError("To be implemented by developer")

    async def refresh(self) -> OAuthTokens:
        """Force a refresh with the refresh token and save the result.

        Callers normally use ``get_access_token()``. Call this directly only when
        the API answered 401 with a token you believed was valid. The caller
        must hold ``self._lock`` or accept a possible duplicate refresh.

        Returns:
            The new ``OAuthTokens``.

        Raises:
            AuthenticationError: No refresh token is stored or seeded, or
                ``invalid_grant`` or ``invalid_client`` from Google.
                Usually means the refresh token was revoked, or unused for 6
                months, and the one time setup must be repeated.
            NestConnectionError: Network failure.
            ServerError: 5xx from the token endpoint.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Get the refresh token with ``await self._current_refresh_token()``.
            2. POST to ``self._token_url`` with ``client_id``, ``client_secret``,
               ``refresh_token``, and ``grant_type=refresh_token`` (see the
               "Refresh an access token" section of the doc).
            3. Parse the body into ``TokenResponse``.
            4. Compute ``expires_at`` as ``clock() + expires_in`` seconds.
            5. Use ``response.refresh_token`` if Google rotated it, otherwise keep
               the one from step 1. Refresh responses usually omit it.
            6. Save the new ``OAuthTokens`` to the store and return them. From
               here on the store, not the seed, holds the refresh token.
            7. Map httpx errors and non 2xx responses to ``NestError`` subclasses.
            Docs: https://developers.google.com/nest/device-access/authorize
        """
        raise NotImplementedError("To be implemented by developer")

    async def _current_refresh_token(self) -> SecretStr:
        """Return the refresh token to use, preferring the store over the seed.

        Returns:
            The stored refresh token, or the seed when the store is empty.

        Raises:
            AuthenticationError: The store is empty and no seed was given. The
                message tells the user to run ``nest-auth url`` and
                ``nest-auth exchange``.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. ``tokens = await self._store.load()``; if not ``None``, return
               ``tokens.refresh_token``.
            2. Else, if ``self._seed_refresh_token`` is set, return it.
            3. Else raise ``AuthenticationError`` with the setup instructions.
        """
        raise NotImplementedError("To be implemented by developer")

    def _is_stale(self, tokens: OAuthTokens) -> bool:
        """Decide whether a cached token should be refreshed now.

        Args:
            tokens: The cached token set.

        Returns:
            ``True`` when ``clock() >= tokens.expires_at - refresh_margin``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Compare against ``self._clock()``, never ``datetime.now()``, so
               tests can move time.
        """
        raise NotImplementedError("To be implemented by developer")
