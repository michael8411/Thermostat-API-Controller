"""``nest-auth`` command line tool for the one time OAuth setup.

Usage once implemented::

    nest-auth url               Print the PCM consent URL.
    nest-auth exchange CODE     Exchange the code and save the tokens.

Reads ``OAuthClientSettings`` from the environment, so the refresh token does
not need to exist yet.

Where ``exchange`` puts the tokens depends on the ``store`` passed to ``main``:

- A ``TokenStore`` (for example a future keyring store): the tokens are saved
  there and the refresh token is never printed. This is the intended path.
- ``None`` (the default until a persistent store exists): the refresh token is
  printed once so the user can seed ``NEST_REFRESH_TOKEN``.

Source: https://developers.google.com/nest/device-access/authorize
"""

import argparse
from collections.abc import Sequence

from py_nest_controller.auth.protocols import TokenStore
from py_nest_controller.config import OAuthClientSettings
from py_nest_controller.models.oauth import OAuthTokens


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser with ``url`` and ``exchange`` subcommands.

    Returns:
        The configured parser.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Create a parser with ``prog="nest-auth"``.
        2. Add required subparsers: ``url`` (optional ``--state``) and
           ``exchange`` (positional ``code``).
    """
    raise NotImplementedError("To be implemented by developer")


async def run_exchange(
    settings: OAuthClientSettings,
    code: str,
    *,
    store: TokenStore | None = None,
) -> OAuthTokens:
    """Exchange ``code`` for tokens and save them when a store is given.

    Args:
        settings: OAuth client settings.
        code: Authorization code copied from the redirect URL.
        store: Where to save the tokens. ``None`` saves nothing and leaves it
            to the caller to show the refresh token.

    Returns:
        The full ``OAuthTokens`` from the exchange.

    Raises:
        AuthenticationError: The exchange failed or returned no refresh token.
        NestConnectionError: Network failure.
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Open an ``httpx.AsyncClient`` in an ``async with`` block.
        2. Call ``exchange_authorization_code`` with the settings values.
        3. Build ``OAuthTokens`` from the response: ``expires_at`` is
           ``datetime.now(UTC) + expires_in`` seconds, and ``refresh_token`` is
           guaranteed present by step 2.
        4. If ``store`` is not ``None``, ``await store.save(tokens)``.
        5. Return the tokens.
    """
    raise NotImplementedError("To be implemented by developer")


def main(argv: Sequence[str] | None = None, *, store: TokenStore | None = None) -> int:
    """Entry point for the ``nest-auth`` console script.

    Args:
        argv: Arguments without the program name. ``None`` means ``sys.argv[1:]``.
        store: Where ``exchange`` saves tokens. The console script passes
            ``None`` until a persistent store exists; tests pass an
            ``InMemoryTokenStore``.

    Returns:
        Process exit code: 0 on success, non zero on any ``NestError``.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Parse ``argv`` with ``build_parser()``.
        2. Load settings with ``load_oauth_client_settings()``.
        3. ``url``: print ``build_authorization_url(...)`` and short instructions
           to copy the ``code`` param from the page you land on.
        4. ``exchange``: run ``run_exchange(..., store=store)`` with ``asyncio.run``.
           With a store, print only a confirmation that the tokens were saved.
           Without one, print the refresh token once with a reminder that it
           is a secret and can seed ``NEST_REFRESH_TOKEN``.
        5. Catch ``NestError``, print its message to stderr, return 1.
        Docs: https://developers.google.com/nest/device-access/authorize
    """
    raise NotImplementedError("To be implemented by developer")
