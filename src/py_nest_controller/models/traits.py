"""One model per device trait, plus the ``traits`` container.

Every field is optional. A trait missing from a GET response means the device
does not support it right now (the Fan trait only exists when the thermostat
controls a fan), and a field missing inside a trait means the API did not send
it in the current state (for example setpoints are omitted in MANUAL_ECO).

All temperatures are Celsius regardless of the display scale.

Source: https://developers.google.com/nest/device-access/api/thermostat
"""

from pydantic import AwareDatetime, Field

from py_nest_controller.models.base import SdmModel
from py_nest_controller.models.enums import (
    ConnectivityStatus,
    EcoMode,
    FanTimerMode,
    HvacStatus,
    TemperatureScale,
    ThermostatMode,
    TraitName,
)


class InfoTrait(SdmModel):
    """``sdm.devices.traits.Info``: the name the user gave the device in the Home app.

    Source: https://developers.google.com/nest/device-access/traits/device/info
    """

    custom_name: str | None = Field(default=None, alias="customName")


class SettingsTrait(SdmModel):
    """``sdm.devices.traits.Settings``: display scale. Cannot be changed through the API.

    Source: https://developers.google.com/nest/device-access/traits/device/settings
    """

    temperature_scale: TemperatureScale | None = Field(default=None, alias="temperatureScale")


class ConnectivityTrait(SdmModel):
    """``sdm.devices.traits.Connectivity``: whether the device is online.

    Source: https://developers.google.com/nest/device-access/traits/device/connectivity
    """

    status: ConnectivityStatus | None = None


class TemperatureTrait(SdmModel):
    """``sdm.devices.traits.Temperature``: ambient temperature in Celsius.

    Source: https://developers.google.com/nest/device-access/traits/device/temperature
    """

    ambient_temperature_celsius: float | None = Field(
        default=None, alias="ambientTemperatureCelsius"
    )


class HumidityTrait(SdmModel):
    """``sdm.devices.traits.Humidity``: ambient relative humidity, 0 to 100 percent.

    Source: https://developers.google.com/nest/device-access/traits/device/humidity
    """

    ambient_humidity_percent: float | None = Field(
        default=None, alias="ambientHumidityPercent", ge=0, le=100
    )


class ThermostatModeTrait(SdmModel):
    """``sdm.devices.traits.ThermostatMode``: current mode and the modes this device allows.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-mode
    """

    mode: ThermostatMode | None = None
    available_modes: tuple[ThermostatMode, ...] = Field(default=(), alias="availableModes")


class ThermostatEcoTrait(SdmModel):
    """``sdm.devices.traits.ThermostatEco``: Eco state and the Eco setpoints.

    ``heat_celsius`` and ``cool_celsius`` are the user's Eco thresholds. They
    are read only through the API.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-eco
    """

    mode: EcoMode | None = None
    available_modes: tuple[EcoMode, ...] = Field(default=(), alias="availableModes")
    heat_celsius: float | None = Field(default=None, alias="heatCelsius")
    cool_celsius: float | None = Field(default=None, alias="coolCelsius")


class ThermostatHvacTrait(SdmModel):
    """``sdm.devices.traits.ThermostatHvac``: what the equipment is doing now.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-hvac
    """

    status: HvacStatus | None = None


class ThermostatTemperatureSetpointTrait(SdmModel):
    """``sdm.devices.traits.ThermostatTemperatureSetpoint``: target temperatures.

    Only the value(s) for the current mode are returned: ``heat_celsius`` in
    HEAT, ``cool_celsius`` in COOL, both in HEATCOOL, neither in OFF or
    MANUAL_ECO.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-temperature-setpoint
    """

    heat_celsius: float | None = Field(default=None, alias="heatCelsius")
    cool_celsius: float | None = Field(default=None, alias="coolCelsius")


class FanTrait(SdmModel):
    """``sdm.devices.traits.Fan``: fan timer state. Present only if the system has a fan.

    ``timer_timeout`` is an RFC 3339 timestamp of when the timer turns OFF.

    Source: https://developers.google.com/nest/device-access/traits/device/fan
    """

    timer_mode: FanTimerMode | None = Field(default=None, alias="timerMode")
    timer_timeout: AwareDatetime | None = Field(default=None, alias="timerTimeout")


class DeviceTraits(SdmModel):
    """The ``traits`` object of a device, keyed by fully qualified trait name.

    Each attribute is ``None`` when its trait is absent from the response.
    Trait keys from other device types are ignored.

    Source: https://developers.google.com/nest/device-access/api/thermostat
    """

    info: InfoTrait | None = Field(default=None, alias=TraitName.INFO.value)
    settings: SettingsTrait | None = Field(default=None, alias=TraitName.SETTINGS.value)
    connectivity: ConnectivityTrait | None = Field(default=None, alias=TraitName.CONNECTIVITY.value)
    temperature: TemperatureTrait | None = Field(default=None, alias=TraitName.TEMPERATURE.value)
    humidity: HumidityTrait | None = Field(default=None, alias=TraitName.HUMIDITY.value)
    thermostat_mode: ThermostatModeTrait | None = Field(
        default=None, alias=TraitName.THERMOSTAT_MODE.value
    )
    thermostat_eco: ThermostatEcoTrait | None = Field(
        default=None, alias=TraitName.THERMOSTAT_ECO.value
    )
    thermostat_hvac: ThermostatHvacTrait | None = Field(
        default=None, alias=TraitName.THERMOSTAT_HVAC.value
    )
    thermostat_temperature_setpoint: ThermostatTemperatureSetpointTrait | None = Field(
        default=None, alias=TraitName.THERMOSTAT_TEMPERATURE_SETPOINT.value
    )
    fan: FanTrait | None = Field(default=None, alias=TraitName.FAN.value)

    def present(self) -> frozenset[TraitName]:
        """Return the set of traits that were present in the response.

        Returns:
            The ``TraitName`` of every attribute above that is not ``None``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Walk the model fields and pick those whose value is not ``None``.
            2. Turn each field's alias back into a ``TraitName``.
            3. ``Thermostat.supports()`` and ``ThermostatState`` both rely on this.
        """
        raise NotImplementedError("To be implemented by developer")
