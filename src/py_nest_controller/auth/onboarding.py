"""One time OAuth setup: PCM consent URL and authorization code exchange.

Run once per account to get a refresh token. After that the SDK only ever
uses the refresh token.

Source: https://developers.google.com/nest/device-access/authorize
"""

import httpx
from pydantic import SecretStr

from py_nest_controller.constants import DEFAULT_REDIRECT_URI, OAUTH_TOKEN_URL
from py_nest_controller.models.oauth import TokenResponse


def build_authorization_url(
    *,
    device_access_project_id: str,
    client_id: str,
    redirect_uri: str = DEFAULT_REDIRECT_URI,
    state: str | None = None,
) -> str:
    """Build the Partner Connections Manager URL the user opens to grant access.

    Args:
        device_access_project_id: Device Access project UUID (not the Cloud project ID).
        client_id: OAuth 2.0 client ID.
        redirect_uri: Must exactly match a redirect URI on the OAuth client.
        state: Optional opaque value echoed back on the redirect, for CSRF checks.

    Returns:
        The full consent URL.

    Raises:
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Format ``constants.PCM_AUTH_URL_TEMPLATE`` with the Device Access project ID.
        2. Add query params: ``redirect_uri``, ``access_type=offline``,
           ``prompt=consent``, ``client_id``, ``response_type=code``, and
           ``scope`` set to ``constants.SDM_OAUTH_SCOPE``; add ``state`` if given.
        3. URL encode the params with the standard library.
        4. ``access_type=offline`` and ``prompt=consent`` are what make Google
           return a refresh token in the next step.
        Docs: https://developers.google.com/nest/device-access/authorize
        (section "Link your account")
    """
    raise NotImplementedError("To be implemented by developer")


async def exchange_authorization_code(
    *,
    client_id: str,
    client_secret: SecretStr,
    code: str,
    http_client: httpx.AsyncClient,
    redirect_uri: str = DEFAULT_REDIRECT_URI,
    token_url: str = OAUTH_TOKEN_URL,
) -> TokenResponse:
    """Trade the one time authorization code for access and refresh tokens.

    Args:
        client_id: OAuth 2.0 client ID.
        client_secret: OAuth 2.0 client secret.
        code: The ``code`` query value from the redirect after consent.
        http_client: Client used for the POST. Not closed here.
        redirect_uri: Same redirect URI used in the authorization URL.
        token_url: Token endpoint. Override only in tests.

    Returns:
        The parsed token response. ``refresh_token`` must be present.

    Raises:
        AuthenticationError: Google rejected the code (expired, reused, or
            redirect URI mismatch), or no refresh token came back.
        NestConnectionError: Network failure.
        ServerError: 5xx from the token endpoint.
        NotImplementedError: Until implemented.

    Implementation notes:
        1. POST to ``token_url`` with ``client_id``, ``client_secret``, ``code``,
           ``grant_type=authorization_code``, and ``redirect_uri``.
        2. Parse the body into ``TokenResponse``.
        3. If ``refresh_token`` is missing, raise ``AuthenticationError``
           explaining to revoke access and redo consent with ``prompt=consent``.
        4. Codes are single use and short lived; exchange right away.
        5. Remind the user that setup is only complete after one
           ``devices.list`` call with the new access token.
        Docs: https://developers.google.com/nest/device-access/authorize
        (section "Get an access token")
    """
    raise NotImplementedError("To be implemented by developer")
