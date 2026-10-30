"""OAuth token shapes: the raw Google token response and the cached token set.

Source: https://developers.google.com/nest/device-access/authorize
"""

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, SecretStr


class TokenResponse(BaseModel):
    """Body returned by Google's token endpoint for code exchange and refresh.

    ``refresh_token`` is only returned by the authorization code exchange (and
    only when ``access_type=offline`` and ``prompt=consent`` were used). Refresh
    responses omit it.

    Source: https://developers.google.com/nest/device-access/authorize
    """

    model_config = ConfigDict(frozen=True, extra="ignore")

    access_token: SecretStr
    expires_in: int = Field(gt=0)
    token_type: str
    scope: str | None = None
    refresh_token: SecretStr | None = None


class OAuthTokens(BaseModel):
    """The token set the manager caches and a ``TokenStore`` persists.

    Attributes:
        access_token: Current bearer token.
        expires_at: Absolute UTC expiry computed from ``expires_in`` at receipt time.
        refresh_token: Long lived token used to mint new access tokens.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    access_token: SecretStr
    expires_at: AwareDatetime
    refresh_token: SecretStr
