"""``nest-auth`` command line tool for the one time OAuth setup.

Usage once implemented::

    nest-auth url               Print the PCM consent URL.
    nest-auth exchange CODE     Exchange the code and print the refresh token.

Reads ``OAuthClientSettings`` from the environment, so the refresh token does
not need to exist yet.

Source: https://developers.google.com/nest/device-access/authorize
"""

import argparse
from collections.abc import Sequence

from py_nest_controller.config import OAuthClientSettings


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


async def run_exchange(settings: OAuthClientSettings, code: str) -> str:
    """Exchange ``code`` for tokens and return the refresh token.

    Args:
        settings: OAuth client settings.
        code: Authorization code copied from the redirect URL.

    Returns:
        The refresh token as a plain string, for the user to put in ``.env``.

    Raises:
        AuthenticationError: The exchange failed or returned no refresh token.
        NestConnectionError: Network failure.
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Open an ``httpx.AsyncClient`` in an ``async with`` block.
        2. Call ``exchange_authorization_code`` with the settings values.
        3. Return ``refresh_token.get_secret_value()``.
    """
    raise NotImplementedError("To be implemented by developer")


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the ``nest-auth`` console script.

    Args:
        argv: Arguments without the program name. ``None`` means ``sys.argv[1:]``.

    Returns:
        Process exit code: 0 on success, non zero on any ``NestError``.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Parse ``argv`` with ``build_parser()``.
        2. Load settings with ``load_oauth_client_settings()``.
        3. ``url``: print ``build_authorization_url(...)`` and short instructions
           to copy the ``code`` param from the page you land on.
        4. ``exchange``: run ``run_exchange`` with ``asyncio.run`` and print the
           refresh token with a reminder to store it as ``NEST_REFRESH_TOKEN``.
        5. Catch ``NestError``, print its message to stderr, return 1.
        Docs: https://developers.google.com/nest/device-access/authorize
    """
    raise NotImplementedError("To be implemented by developer")
