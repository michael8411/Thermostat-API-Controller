"""High level thermostat API. This is the main public surface of the SDK.

``Thermostat`` turns SDM rules into clear errors before a command is sent,
then still handles the server's verdict, because state can change between
the check and the command.

Source: https://developers.google.com/nest/device-access/api/thermostat
"""

from datetime import timedelta

from py_nest_controller.client.sdm import SDMClient
from py_nest_controller.models.enums import ThermostatMode, TraitName
from py_nest_controller.models.resources import Device
from py_nest_controller.models.state import ThermostatState


class Thermostat:
    """One Nest thermostat, identified by its device ID, using a shared ``SDMClient``.

    All temperatures are Celsius. Convert at the edge with ``py_nest_controller.units``.

    Rate limits to keep in mind (Sandbox): 5 commands per minute per device,
    100 per hour for thermostats, and 10 ``devices.get`` per minute. Prefer
    reusing the last fetched state for precondition checks instead of a GET
    before every command.

    Source: https://developers.google.com/nest/device-access/project/limits
    """

    _client: SDMClient
    _device_id: str
    _last_device: Device | None

    def __init__(self, client: SDMClient, device_id: str) -> None:
        """Wrap one device. Makes no network calls.

        Args:
            client: Shared low level client.
            device_id: Bare device ID (last segment of the resource name).

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Store both arguments and set ``_last_device`` to ``None``.
        """
        raise NotImplementedError("To be implemented by developer")

    @property
    def device_id(self) -> str:
        """The bare device ID this instance controls.

        Returns:
            The device ID.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Return ``self._device_id``.
        """
        raise NotImplementedError("To be implemented by developer")

    async def get_state(self) -> ThermostatState:
        """Fetch the device and return a fresh snapshot.

        Returns:
            A frozen ``ThermostatState`` with ambient temperature, humidity,
            mode, Eco, HVAC status, setpoints, fan, and connectivity.

        Raises:
            NotFoundError: Device no longer exists or was unshared.
            RateLimitedError: Too many ``devices.get`` calls.
            AuthenticationError: Token rejected.
            ServerError: 5xx.
            NestConnectionError: Network failure.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. ``await self._client.get_device(self._device_id)``.
            2. Cache the result in ``_last_device`` for ``supports()`` and
               precondition checks.
            3. Return ``ThermostatState.from_device(device, fetched_at=now_utc)``.
            Docs: https://developers.google.com/nest/device-access/api/thermostat
        """
        raise NotImplementedError("To be implemented by developer")

    async def supports(self, trait: TraitName, *, refresh: bool = False) -> bool:
        """Check whether the device currently exposes a trait.

        Args:
            trait: The trait to check, for example ``TraitName.FAN``.
            refresh: Fetch the device first even if a cached copy exists.

        Returns:
            ``True`` if the trait was present in the latest GET response.

        Raises:
            NestError: Any error from ``get_state()`` when a fetch is needed.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. If ``refresh`` or nothing is cached, call ``get_state()``.
            2. Check ``trait in self._last_device.traits.present()``.
            3. A missing trait means unsupported right now; the Fan trait is
               absent when the system has no fan.
            Docs: https://developers.google.com/nest/device-access/api/thermostat
        """
        raise NotImplementedError("To be implemented by developer")

    async def set_mode(self, mode: ThermostatMode) -> None:
        """Change the thermostat mode to HEAT, COOL, HEATCOOL, or OFF.

        Does not touch Eco. If Eco is MANUAL_ECO, turn it off with
        ``set_eco(False)`` first or the device stays in Eco.

        Args:
            mode: Target mode. Must be in the device's ``available_modes``.

        Raises:
            UnsupportedTraitError: No ThermostatMode trait.
            InvalidArgumentError: ``mode`` not in ``available_modes``.
            FailedPreconditionError: The device rejected the change.
            DeviceOfflineError: Device is offline.
            RateLimitedError: Command quota exceeded.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Ensure the ThermostatMode trait is present.
            2. Check ``mode`` against ``available_modes`` from the cached device.
            3. Send ``SetThermostatModeCommand(mode=mode)``.
            4. Clear or refresh the cached device; it is now stale.
            Docs: https://developers.google.com/nest/device-access/traits/device/thermostat-mode
        """
        raise NotImplementedError("To be implemented by developer")

    async def set_heat(self, celsius: float) -> None:
        """Set the heat setpoint. Only valid in HEAT mode.

        Args:
            celsius: Target temperature in Celsius.

        Raises:
            FailedPreconditionError: Mode is not HEAT, or Eco is MANUAL_ECO.
            UnsupportedTraitError: No ThermostatTemperatureSetpoint trait.
            DeviceOfflineError: Device is offline.
            RateLimitedError: Command quota exceeded.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Using the cached state, raise ``FailedPreconditionError`` early if
               Eco is MANUAL_ECO or mode is not HEAT. Say which mode is needed.
            2. Send ``SetHeatCommand(heat_celsius=celsius)``.
            3. Still expect FAILED_PRECONDITION from the server if state changed.
            Docs: https://developers.google.com/nest/device-access/traits/device/thermostat-temperature-setpoint
        """
        raise NotImplementedError("To be implemented by developer")

    async def set_cool(self, celsius: float) -> None:
        """Set the cool setpoint. Only valid in COOL mode.

        Args:
            celsius: Target temperature in Celsius.

        Raises:
            FailedPreconditionError: Mode is not COOL, or Eco is MANUAL_ECO.
            UnsupportedTraitError: No ThermostatTemperatureSetpoint trait.
            DeviceOfflineError: Device is offline.
            RateLimitedError: Command quota exceeded.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Same checks as ``set_heat`` but require COOL.
            2. Send ``SetCoolCommand(cool_celsius=celsius)``.
            Docs: https://developers.google.com/nest/device-access/traits/device/thermostat-temperature-setpoint
        """
        raise NotImplementedError("To be implemented by developer")

    async def set_range(self, heat_celsius: float, cool_celsius: float) -> None:
        """Set both setpoints. Only valid in HEATCOOL mode.

        Args:
            heat_celsius: Heat below this temperature, in Celsius.
            cool_celsius: Cool above this temperature, in Celsius. Must be
                greater than ``heat_celsius``.

        Raises:
            InvalidArgumentError: ``heat_celsius >= cool_celsius``.
            FailedPreconditionError: Mode is not HEATCOOL, or Eco is MANUAL_ECO.
            UnsupportedTraitError: No ThermostatTemperatureSetpoint trait.
            DeviceOfflineError: Device is offline.
            RateLimitedError: Command quota exceeded.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Validate heat < cool locally and raise ``InvalidArgumentError``.
            2. Same mode and Eco checks as ``set_heat`` but require HEATCOOL.
            3. Send ``SetRangeCommand``.
            Docs: https://developers.google.com/nest/device-access/traits/device/thermostat-temperature-setpoint
        """
        raise NotImplementedError("To be implemented by developer")

    async def set_eco(self, enabled: bool) -> None:
        """Turn manual Eco on or off.

        While Eco is on, setpoints cannot be changed and the setpoint trait
        returns no values. The Eco thresholds themselves are read only.
        Turning Eco off returns the device to its last standard mode.

        Args:
            enabled: ``True`` for MANUAL_ECO, ``False`` for OFF.

        Raises:
            UnsupportedTraitError: No ThermostatEco trait, or the target Eco
                mode is not in ``available_modes``.
            FailedPreconditionError: Some models reject Eco changes while the
                thermostat mode is OFF.
            DeviceOfflineError: Device is offline.
            RateLimitedError: Command quota exceeded.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Map ``enabled`` to ``EcoMode.MANUAL_ECO`` or ``EcoMode.OFF``.
            2. Check the Eco trait and its ``available_modes``.
            3. Send ``SetEcoModeCommand``. Do not pre-block mode OFF; let the
               server decide, since only some models reject it.
            Docs: https://developers.google.com/nest/device-access/traits/device/thermostat-eco
        """
        raise NotImplementedError("To be implemented by developer")

    async def start_fan(self, duration: timedelta | None = None) -> None:
        """Run the fan for a period of time.

        Args:
            duration: How long to run, from 1 second to 12 hours. ``None``
                lets the API use its default of 15 minutes.

        Raises:
            UnsupportedTraitError: No Fan trait (system has no fan).
            InvalidArgumentError: ``duration`` outside 1s to 43200s.
            FailedPreconditionError: "Thermostat fan unavailable." from the server.
            DeviceOfflineError: Device is offline.
            RateLimitedError: Command quota exceeded.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Check ``supports(TraitName.FAN)`` and raise ``UnsupportedTraitError`` if absent.
            2. Build ``SetFanTimerCommand(timer_mode=ON, duration=duration)``;
               convert a Pydantic ``ValidationError`` to ``InvalidArgumentError``.
            3. Send it.
            Docs: https://developers.google.com/nest/device-access/traits/device/fan
        """
        raise NotImplementedError("To be implemented by developer")

    async def stop_fan(self) -> None:
        """Stop the fan timer.

        Raises:
            UnsupportedTraitError: No Fan trait.
            FailedPreconditionError: Rejected by the server.
            DeviceOfflineError: Device is offline.
            RateLimitedError: Command quota exceeded.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Check the Fan trait as in ``start_fan``.
            2. Send ``SetFanTimerCommand(timer_mode=OFF)`` with no duration.
            Docs: https://developers.google.com/nest/device-access/traits/device/fan
        """
        raise NotImplementedError("To be implemented by developer")

    async def _require_trait(self, trait: TraitName) -> Device:
        """Return the cached device, raising if it lacks ``trait`` or is offline.

        Args:
            trait: Trait the caller is about to use.

        Returns:
            The cached (or freshly fetched) ``Device``.

        Raises:
            UnsupportedTraitError: Trait absent.
            DeviceOfflineError: Connectivity reports OFFLINE.
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Fetch if nothing is cached.
            2. Raise ``DeviceOfflineError`` when Connectivity is OFFLINE.
            3. Raise ``UnsupportedTraitError`` naming the trait when absent.
        """
        raise NotImplementedError("To be implemented by developer")
