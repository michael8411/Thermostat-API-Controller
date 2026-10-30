"""The frozen thermostat snapshot returned to consumers.

``ThermostatState`` flattens the trait models into one object with plain
fields so callers never deal with trait keys or aliases. It is the stable
read model for scripts, dashboards, and any other consumer.
"""

from datetime import datetime

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from py_nest_controller.models.enums import (
    ConnectivityStatus,
    EcoMode,
    FanTimerMode,
    HvacStatus,
    TemperatureScale,
    ThermostatMode,
    TraitName,
)
from py_nest_controller.models.resources import Device


class ThermostatState(BaseModel):
    """Point in time view of one thermostat. All temperatures are Celsius.

    Fields are ``None`` when the device did not report them, either because the
    trait is unsupported (check ``supported_traits``) or because the current
    mode hides them (setpoints in OFF and MANUAL_ECO).

    Attributes:
        device_id: Bare device ID.
        name: Full resource name ``enterprises/{project}/devices/{device}``.
        custom_name: Name from the Home app (Info trait).
        connectivity: ONLINE or OFFLINE.
        ambient_temperature_celsius: Measured temperature.
        ambient_humidity_percent: Measured relative humidity, 0 to 100.
        display_scale: Scale shown on the device. Display only.
        mode: Current thermostat mode.
        available_modes: Modes this device accepts in ``set_mode``.
        eco_mode: Current Eco mode.
        available_eco_modes: Eco modes this device accepts.
        eco_heat_celsius: Eco heat threshold (read only).
        eco_cool_celsius: Eco cool threshold (read only).
        hvac_status: What the equipment is doing now.
        heat_setpoint_celsius: Heat target (HEAT and HEATCOOL only).
        cool_setpoint_celsius: Cool target (COOL and HEATCOOL only).
        fan_timer_mode: Fan timer state, ``None`` if there is no fan.
        fan_timer_timeout: When the fan timer turns off.
        supported_traits: Traits present in the response.
        fetched_at: When the snapshot was taken (UTC).
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    device_id: str
    name: str
    custom_name: str | None = None
    connectivity: ConnectivityStatus | None = None
    ambient_temperature_celsius: float | None = None
    ambient_humidity_percent: float | None = Field(default=None, ge=0, le=100)
    display_scale: TemperatureScale | None = None
    mode: ThermostatMode | None = None
    available_modes: tuple[ThermostatMode, ...] = ()
    eco_mode: EcoMode | None = None
    available_eco_modes: tuple[EcoMode, ...] = ()
    eco_heat_celsius: float | None = None
    eco_cool_celsius: float | None = None
    hvac_status: HvacStatus | None = None
    heat_setpoint_celsius: float | None = None
    cool_setpoint_celsius: float | None = None
    fan_timer_mode: FanTimerMode | None = None
    fan_timer_timeout: AwareDatetime | None = None
    supported_traits: frozenset[TraitName] = frozenset()
    fetched_at: AwareDatetime

    @classmethod
    def from_device(cls, device: Device, *, fetched_at: datetime) -> "ThermostatState":
        """Flatten a parsed ``Device`` into a snapshot.

        Args:
            device: Device parsed from a ``devices.get`` or ``devices.list`` response.
            fetched_at: Timezone aware time the response was received.

        Returns:
            A new frozen ``ThermostatState``.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Copy ``device.name`` and ``device.device_id``.
            2. For each trait on ``device.traits``, copy its fields if the trait
               is present, otherwise leave the snapshot field as ``None``.
            3. Fill ``supported_traits`` from ``device.traits.present()``.
            4. Do no I/O and no unit conversion here.
            Docs: https://developers.google.com/nest/device-access/api/thermostat
        """
        raise NotImplementedError("To be implemented by developer")

    @property
    def is_eco_active(self) -> bool:
        """Whether manual Eco is on, which blocks setpoint changes.

        Returns:
            ``True`` when ``eco_mode`` is MANUAL_ECO.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Compare ``eco_mode`` with ``EcoMode.MANUAL_ECO``.
            Docs: https://developers.google.com/nest/device-access/traits/device/thermostat-eco
        """
        raise NotImplementedError("To be implemented by developer")

    @property
    def is_online(self) -> bool:
        """Whether the device reported ONLINE.

        Returns:
            ``True`` only when ``connectivity`` is ONLINE.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Treat a missing Connectivity trait as unknown, not offline; decide
               and document which way your code leans.
            Docs: https://developers.google.com/nest/device-access/traits/device/connectivity
        """
        raise NotImplementedError("To be implemented by developer")
