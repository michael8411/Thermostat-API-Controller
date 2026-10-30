"""One request model per SDM command.

Each class carries its exact fully qualified command name in ``COMMAND_NAME``
and declares its params as fields. ``to_request_body()`` turns it into the
``executeCommand`` body.

Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/executeCommand
"""

from datetime import timedelta
from typing import Annotated, Any, ClassVar

from pydantic import Field

from py_nest_controller.constants import FAN_TIMER_MAX_DURATION, FAN_TIMER_MIN_DURATION
from py_nest_controller.models.base import SdmModel
from py_nest_controller.models.enums import EcoMode, FanTimerMode, ThermostatMode

FanDuration = Annotated[timedelta, Field(ge=FAN_TIMER_MIN_DURATION, le=FAN_TIMER_MAX_DURATION)]
"""A fan timer length between 1 second and 12 hours, inclusive."""


class ExecuteCommandRequest(SdmModel):
    """The ``executeCommand`` request body.

    Attributes:
        command: Fully qualified command name.
        params: Command params with camelCase keys.

    Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/executeCommand
    """

    command: str
    params: dict[str, Any] = Field(default_factory=dict)


class SdmCommand(SdmModel):
    """Base class for every command. Subclasses set ``COMMAND_NAME`` and declare params."""

    COMMAND_NAME: ClassVar[str]

    def to_request_body(self) -> ExecuteCommandRequest:
        """Build the ``executeCommand`` body for this command.

        Returns:
            An ``ExecuteCommandRequest`` with ``command`` set to ``COMMAND_NAME``
            and ``params`` set to this model's fields using their JSON aliases.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Dump this model by alias, in JSON mode, excluding ``None`` values
               so optional params (like fan ``duration``) are omitted.
            2. Wrap the result with ``COMMAND_NAME`` in an ``ExecuteCommandRequest``.
            3. The client then sends ``model_dump(by_alias=True)`` of that object.
            Docs: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/executeCommand
        """
        raise NotImplementedError("To be implemented by developer")


class SetThermostatModeCommand(SdmCommand):
    """``ThermostatMode.SetMode``: switch between HEAT, COOL, HEATCOOL, and OFF.

    Does not control Eco. The mode must be one of the device's ``availableModes``.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-mode
    """

    COMMAND_NAME: ClassVar[str] = "sdm.devices.commands.ThermostatMode.SetMode"

    mode: ThermostatMode


class SetEcoModeCommand(SdmCommand):
    """``ThermostatEco.SetMode``: turn manual Eco on (MANUAL_ECO) or off (OFF).

    Turning Eco OFF returns the thermostat to its last standard mode. Some
    models reject this while the thermostat mode is OFF (FAILED_PRECONDITION).

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-eco
    """

    COMMAND_NAME: ClassVar[str] = "sdm.devices.commands.ThermostatEco.SetMode"

    mode: EcoMode


class SetHeatCommand(SdmCommand):
    """``ThermostatTemperatureSetpoint.SetHeat``: heat target in Celsius. Needs mode HEAT.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-temperature-setpoint
    """

    COMMAND_NAME: ClassVar[str] = "sdm.devices.commands.ThermostatTemperatureSetpoint.SetHeat"

    heat_celsius: float = Field(alias="heatCelsius")


class SetCoolCommand(SdmCommand):
    """``ThermostatTemperatureSetpoint.SetCool``: cool target in Celsius. Needs mode COOL.

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-temperature-setpoint
    """

    COMMAND_NAME: ClassVar[str] = "sdm.devices.commands.ThermostatTemperatureSetpoint.SetCool"

    cool_celsius: float = Field(alias="coolCelsius")


class SetRangeCommand(SdmCommand):
    """``ThermostatTemperatureSetpoint.SetRange``: heat and cool targets. Needs mode HEATCOOL.

    The API requires ``heat_celsius`` to be lower than ``cool_celsius`` and
    returns INVALID_ARGUMENT otherwise.

    Implementation notes:
        1. Add a ``model_validator(mode="after")`` that rejects
           ``heat_celsius >= cool_celsius`` so the mistake is caught locally.
        2. Decide whether a ``ValueError`` from that validator should surface
           as ``InvalidArgumentError`` at the ``Thermostat`` layer (it should).

    Source: https://developers.google.com/nest/device-access/traits/device/thermostat-temperature-setpoint
    """

    COMMAND_NAME: ClassVar[str] = "sdm.devices.commands.ThermostatTemperatureSetpoint.SetRange"

    heat_celsius: float = Field(alias="heatCelsius")
    cool_celsius: float = Field(alias="coolCelsius")


class SetFanTimerCommand(SdmCommand):
    """``Fan.SetTimer``: start (ON) or stop (OFF) the fan timer.

    ``duration`` is optional; the API runs 15 minutes when it is omitted. On
    the wire it is a string of whole seconds with an ``s`` suffix, for example
    ``"3600s"``, between ``"1s"`` and ``"43200s"``.

    Implementation notes:
        1. Add a ``field_serializer("duration")`` that renders the timedelta
           as whole seconds followed by ``s``.
        2. Send ``duration`` only with ``timer_mode`` ON.
        3. Fails with FAILED_PRECONDITION "Thermostat fan unavailable." when
           the system has no fan.

    Source: https://developers.google.com/nest/device-access/traits/device/fan
    """

    COMMAND_NAME: ClassVar[str] = "sdm.devices.commands.Fan.SetTimer"

    timer_mode: FanTimerMode = Field(alias="timerMode")
    duration: FanDuration | None = None
