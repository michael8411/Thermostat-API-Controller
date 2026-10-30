"""py-nest-controller: typed async SDK for the Google Smart Device Management API.

Everything a consumer needs is importable from here.

Source: https://developers.google.com/nest/device-access
"""

from py_nest_controller import units
from py_nest_controller.auth import (
    InMemoryTokenStore,
    OAuthTokenManager,
    TokenProvider,
    TokenStore,
    build_authorization_url,
    exchange_authorization_code,
)
from py_nest_controller.client import SDMClient
from py_nest_controller.config import (
    NestSettings,
    OAuthClientSettings,
    load_oauth_client_settings,
    load_settings,
)
from py_nest_controller.devices import Thermostat, list_thermostats
from py_nest_controller.exceptions import (
    AuthenticationError,
    ConfigurationError,
    DeviceOfflineError,
    FailedPreconditionError,
    InvalidArgumentError,
    NestConnectionError,
    NestError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
    UnsupportedTraitError,
)
from py_nest_controller.models import (
    ConnectivityStatus,
    Device,
    EcoMode,
    FanTimerMode,
    HvacStatus,
    OAuthTokens,
    Structure,
    TemperatureScale,
    ThermostatMode,
    ThermostatState,
    TraitName,
)
from py_nest_controller.units import celsius_to_fahrenheit, fahrenheit_to_celsius

__version__ = "0.1.0"

__all__ = [
    "AuthenticationError",
    "ConfigurationError",
    "ConnectivityStatus",
    "Device",
    "DeviceOfflineError",
    "EcoMode",
    "FailedPreconditionError",
    "FanTimerMode",
    "HvacStatus",
    "InMemoryTokenStore",
    "InvalidArgumentError",
    "NestConnectionError",
    "NestError",
    "NestSettings",
    "NotFoundError",
    "OAuthClientSettings",
    "OAuthTokenManager",
    "OAuthTokens",
    "PermissionDeniedError",
    "RateLimitedError",
    "SDMClient",
    "ServerError",
    "Structure",
    "TemperatureScale",
    "Thermostat",
    "ThermostatMode",
    "ThermostatState",
    "TokenProvider",
    "TokenStore",
    "TraitName",
    "UnsupportedTraitError",
    "__version__",
    "build_authorization_url",
    "celsius_to_fahrenheit",
    "exchange_authorization_code",
    "fahrenheit_to_celsius",
    "list_thermostats",
    "load_oauth_client_settings",
    "load_settings",
    "units",
]
