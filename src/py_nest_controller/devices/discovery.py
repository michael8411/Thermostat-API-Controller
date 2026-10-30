"""Find the thermostats on the account.

Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/list
"""

from py_nest_controller.client.sdm import SDMClient
from py_nest_controller.devices.thermostat import Thermostat


async def list_thermostats(client: SDMClient) -> list[Thermostat]:
    """Return a ``Thermostat`` for every thermostat shared with this project.

    Args:
        client: The shared low level client.

    Returns:
        One ``Thermostat`` per device whose type is ``DeviceType.THERMOSTAT``,
        in API order. Empty if none were shared.

    Raises:
        AuthenticationError: Token rejected.
        NotFoundError: Wrong Device Access project ID.
        RateLimitedError: More than 5 ``devices.list`` calls per minute.
        ServerError: 5xx.
        NestConnectionError: Network failure.
        NotImplementedError: Until implemented.

    Implementation notes:
        1. ``await client.list_devices()``.
        2. Keep devices whose ``type`` equals ``DeviceType.THERMOSTAT``. Type is
           fine for discovery; capabilities must still come from traits.
        3. Build ``Thermostat(client, device.device_id)`` for each.
        Docs: https://developers.google.com/nest/device-access/api/thermostat
    """
    raise NotImplementedError("To be implemented by developer")
