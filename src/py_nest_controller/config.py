"""Settings loaded from ``NEST_*`` environment variables (and an optional ``.env`` file).

Two classes exist on purpose:

- ``OAuthClientSettings`` holds what the one time setup needs: the OAuth client
  and the Device Access project ID. The ``nest-auth`` CLI uses it before a
  refresh token exists.
- ``NestSettings`` adds optional values. Everything else in the SDK uses it.

The refresh token is not a setting. It lives in a ``TokenStore``, which
``nest-auth exchange`` writes and ``OAuthTokenManager`` reads. ``NEST_REFRESH_TOKEN``
is only an optional seed for an empty store (first run, CI, a container).

Two different "project IDs" exist in this world and the field names keep them
apart: ``device_access_project_id`` (a UUID from the Device Access Console, used
in every SDM URL) and ``gcp_project_id`` (a Google Cloud project ID, only for
future Pub/Sub). The UUID pattern on the first one makes it impossible to paste
a Cloud project ID there by mistake.

Source: https://developers.google.com/nest/device-access/get-started
"""

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from py_nest_controller.constants import DEFAULT_REDIRECT_URI

UUID_PATTERN = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
"""Shape of a Device Access project ID."""

GCP_PROJECT_ID_PATTERN = r"^[a-z][a-z0-9-]{4,28}[a-z0-9]$"
"""Shape of a Google Cloud project ID: 6 to 30 chars, lowercase, starts with a letter."""


class OAuthClientSettings(BaseSettings):
    """OAuth client and Device Access project. Enough to run the one time setup.

    Environment variables:
        NEST_OAUTH_CLIENT_ID: OAuth 2.0 client ID from Google Cloud Credentials.
        NEST_OAUTH_CLIENT_SECRET: Matching client secret.
        NEST_DEVICE_ACCESS_PROJECT_ID: Device Access project UUID (not the Cloud project ID).
        NEST_REDIRECT_URI: Redirect URI registered on the OAuth client.

    Source: https://developers.google.com/nest/device-access/authorize
    """

    model_config = SettingsConfigDict(
        env_prefix="NEST_",
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
        frozen=True,
    )

    oauth_client_id: str = Field(min_length=1)
    oauth_client_secret: SecretStr
    device_access_project_id: str = Field(pattern=UUID_PATTERN)
    redirect_uri: str = DEFAULT_REDIRECT_URI


class NestSettings(OAuthClientSettings):
    """Full runtime settings for the SDK.

    Environment variables (in addition to ``OAuthClientSettings``):
        NEST_REFRESH_TOKEN: Optional seed refresh token. Used only when the
            ``TokenStore`` is empty. The store is the source of truth.
        NEST_DEFAULT_DEVICE_ID: Optional bare device ID to use when none is given.
        NEST_GCP_PROJECT_ID: Optional Google Cloud project ID. Only needed for
            future Pub/Sub events; nothing reads it today.

    Source: https://developers.google.com/nest/device-access/authorize
    """

    refresh_token: SecretStr | None = None
    default_device_id: str | None = None
    gcp_project_id: str | None = Field(default=None, pattern=GCP_PROJECT_ID_PATTERN)


def load_oauth_client_settings() -> OAuthClientSettings:
    """Load the settings the one time OAuth setup needs.

    Returns:
        Validated ``OAuthClientSettings``.

    Raises:
        ConfigurationError: A required variable is missing or malformed.
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Instantiate ``OAuthClientSettings()``; pydantic-settings reads the
           environment and ``.env``.
        2. Catch ``pydantic.ValidationError`` and re-raise ``ConfigurationError``
           whose message lists each failing field as its ``NEST_`` env var name.
        3. Chain the original error with ``from``.
    """
    raise NotImplementedError("To be implemented by developer")


def load_settings() -> NestSettings:
    """Load and validate full runtime settings, failing fast on anything missing.

    Returns:
        Validated ``NestSettings``.

    Raises:
        ConfigurationError: A required variable is missing or malformed. The
            message names every offending ``NEST_*`` variable at once.
        NotImplementedError: Until implemented.

    Implementation notes:
        1. Instantiate ``NestSettings()``.
        2. Catch ``pydantic.ValidationError``; build one message listing every
           error's field as ``NEST_<FIELD>`` so the user fixes them in one pass.
        3. Never include secret values in the message.
        4. Re-raise as ``ConfigurationError`` chained with ``from``.
    """
    raise NotImplementedError("To be implemented by developer")
