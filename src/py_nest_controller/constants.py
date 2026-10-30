"""Fixed values taken from the SDM and Google OAuth documentation.

This module is a leaf: it imports nothing from the package. Each constant
names the doc page it came from so you can recheck it when Google changes
something.
"""

from datetime import timedelta
from typing import Final

SDM_API_BASE_URL: Final = "https://smartdevicemanagement.googleapis.com/v1"
"""Base URL for every SDM REST call.

Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/executeCommand
"""

ENTERPRISE_PATH_TEMPLATE: Final = "enterprises/{device_access_project_id}"
"""Resource name of the enterprise. The ID is the Device Access project ID.

Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices
"""

PCM_AUTH_URL_TEMPLATE: Final = (
    "https://nestservices.google.com/partnerconnections/{device_access_project_id}/auth"
)
"""Partner Connections Manager consent page. Formatted with the Device Access project ID.

Source: https://developers.google.com/nest/device-access/authorize
"""

OAUTH_TOKEN_URL: Final = "https://www.googleapis.com/oauth2/v4/token"
"""Google token endpoint used for both code exchange and refresh, as given in the SDM guide.

Source: https://developers.google.com/nest/device-access/authorize
"""

SDM_OAUTH_SCOPE: Final = "https://www.googleapis.com/auth/sdm.service"
"""The only OAuth scope the SDM API needs.

Source: https://developers.google.com/nest/device-access/authorize
"""

DEFAULT_REDIRECT_URI: Final = "https://www.google.com"
"""Redirect URI used throughout the SDM guide. Must match the OAuth client config.

Source: https://developers.google.com/nest/device-access/authorize
"""

ACCESS_TOKEN_LIFETIME: Final = timedelta(seconds=3599)
"""Typical access token lifetime (``expires_in``). Always prefer the value Google returns.

Source: https://developers.google.com/nest/device-access/authorize
"""

DEFAULT_TOKEN_REFRESH_MARGIN: Final = timedelta(minutes=5)
"""How long before expiry a cached access token is treated as stale.

A project choice, not a doc value.
"""

FAN_TIMER_MIN_DURATION: Final = timedelta(seconds=1)
"""Shortest allowed ``Fan.SetTimer`` duration.

Source: https://developers.google.com/nest/device-access/traits/device/fan
"""

FAN_TIMER_MAX_DURATION: Final = timedelta(seconds=43200)
"""Longest allowed ``Fan.SetTimer`` duration (12 hours).

Source: https://developers.google.com/nest/device-access/traits/device/fan
"""

FAN_TIMER_DEFAULT_DURATION: Final = timedelta(seconds=900)
"""Duration the API uses when ``duration`` is omitted (15 minutes).

Source: https://developers.google.com/nest/device-access/traits/device/fan
"""

SANDBOX_COMMANDS_PER_MINUTE_PER_DEVICE: Final = 5
"""Sandbox limit for ``devices.executeCommand``. Exceeding it returns RESOURCE_EXHAUSTED.

Source: https://developers.google.com/nest/device-access/project/limits
"""

SANDBOX_THERMOSTAT_COMMANDS_PER_HOUR: Final = 100
"""Device instance limit for thermostat commands, shared across projects.

Source: https://developers.google.com/nest/device-access/project/limits
"""
