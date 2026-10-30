"""Enums for every fixed value set in the thermostat API.

Values are the exact strings the API sends and accepts. ``StrEnum`` members
compare equal to their string value, so they serialize without extra code.
"""

from enum import StrEnum


class ThermostatMode(StrEnum):
    """Thermostat operating mode (ThermostatMode trait ``mode`` and ``availableModes``).

    Eco is not one of these; it is a separate trait. See ``EcoMode``.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-mode
    """

    HEAT = "HEAT"
    COOL = "COOL"
    HEATCOOL = "HEATCOOL"
    OFF = "OFF"


class EcoMode(StrEnum):
    """Eco mode (ThermostatEco trait ``mode`` and ``availableModes``).

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-eco
    """

    MANUAL_ECO = "MANUAL_ECO"
    OFF = "OFF"


class HvacStatus(StrEnum):
    """What the HVAC equipment is doing right now (ThermostatHvac trait ``status``).

    May lag behind a mode change because the system delays to protect equipment.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-hvac
    """

    OFF = "OFF"
    HEATING = "HEATING"
    COOLING = "COOLING"


class FanTimerMode(StrEnum):
    """Fan timer state (Fan trait ``timerMode`` and the SetTimer ``timerMode`` param).

    Source: https://developers.google.com/nest/device-access/traits/device/fan
    """

    ON = "ON"
    OFF = "OFF"


class ConnectivityStatus(StrEnum):
    """Whether the device is reachable (Connectivity trait ``status``).

    Source: https://developers.google.com/nest/device-access/traits/device/connectivity
    """

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"


class TemperatureScale(StrEnum):
    """Display scale on the device (Settings trait ``temperatureScale``). Read only via the API.

    Source: https://developers.google.com/nest/device-access/traits/device/settings
    """

    CELSIUS = "CELSIUS"
    FAHRENHEIT = "FAHRENHEIT"


class DeviceType(StrEnum):
    """Device type strings (Device ``type`` field).

    Use for discovery only. The docs say capabilities must come from traits, not type.

    Source: https://developers.google.com/nest/device-access/api/thermostat
    """

    THERMOSTAT = "sdm.devices.types.THERMOSTAT"


class TraitName(StrEnum):
    """Fully qualified trait keys as they appear under a device's ``traits`` object.

    Pass these to ``Thermostat.supports()``.

    Source: https://developers.google.com/nest/device-access/api/thermostat
    """

    INFO = "sdm.devices.traits.Info"
    SETTINGS = "sdm.devices.traits.Settings"
    CONNECTIVITY = "sdm.devices.traits.Connectivity"
    TEMPERATURE = "sdm.devices.traits.Temperature"
    HUMIDITY = "sdm.devices.traits.Humidity"
    THERMOSTAT_MODE = "sdm.devices.traits.ThermostatMode"
    THERMOSTAT_ECO = "sdm.devices.traits.ThermostatEco"
    THERMOSTAT_HVAC = "sdm.devices.traits.ThermostatHvac"
    THERMOSTAT_TEMPERATURE_SETPOINT = "sdm.devices.traits.ThermostatTemperatureSetpoint"
    FAN = "sdm.devices.traits.Fan"


class StructureTraitName(StrEnum):
    """Fully qualified trait keys under a structure's ``traits`` object.

    Source: https://developers.google.com/nest/device-access/traits/structure/info
    """

    INFO = "sdm.structures.traits.Info"
