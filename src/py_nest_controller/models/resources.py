"""Device, structure, list, command result, and error response models.

Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices
"""

from typing import Any

from pydantic import Field

from py_nest_controller.models.base import SdmModel
from py_nest_controller.models.enums import StructureTraitName
from py_nest_controller.models.traits import DeviceTraits


class ParentRelation(SdmModel):
    """The structure or room a device is assigned to.

    Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices
    """

    parent: str
    display_name: str | None = Field(default=None, alias="displayName")


class Device(SdmModel):
    """One device as returned by ``devices.get`` or inside ``devices.list``.

    ``name`` is the full resource name ``enterprises/{project}/devices/{device}``.
    ``type`` is for display and discovery only; capabilities come from ``traits``.

    Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices
    """

    name: str
    type: str | None = None
    traits: DeviceTraits = Field(default_factory=DeviceTraits)
    parent_relations: tuple[ParentRelation, ...] = Field(default=(), alias="parentRelations")

    @property
    def device_id(self) -> str:
        """The bare device ID: the last path segment of ``name``.

        Returns:
            The device ID string used in ``Thermostat`` and ``SDMClient`` calls.

        Raises:
            NotImplementedError: Until implemented.

        Implementation notes:
            1. Split ``name`` on ``/`` and take the segment after ``devices``.
            2. Do not assume the project ID length; parse by position.
        """
        raise NotImplementedError("To be implemented by developer")


class ListDevicesResponse(SdmModel):
    """Body of ``GET enterprises/{project}/devices``. Empty list when no devices are shared.

    Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/list
    """

    devices: tuple[Device, ...] = ()


class StructureInfoTrait(SdmModel):
    """``sdm.structures.traits.Info``: the structure name shown in the Google Home app.

    Source: https://developers.google.com/nest/device-access/traits/structure/info
    """

    custom_name: str | None = Field(default=None, alias="customName")


class StructureTraits(SdmModel):
    """The ``traits`` object of a structure.

    Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.structures
    """

    info: StructureInfoTrait | None = Field(default=None, alias=StructureTraitName.INFO.value)


class Structure(SdmModel):
    """A home (structure) as returned by ``structures.list``.

    Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.structures
    """

    name: str
    traits: StructureTraits = Field(default_factory=StructureTraits)


class ListStructuresResponse(SdmModel):
    """Body of ``GET enterprises/{project}/structures``.

    Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.structures/list
    """

    structures: tuple[Structure, ...] = ()


class ExecuteCommandResponse(SdmModel):
    """Body of a successful ``executeCommand``. Thermostat commands return an empty object.

    Source: https://developers.google.com/nest/device-access/reference/rest/v1/enterprises.devices/executeCommand
    """

    results: dict[str, Any] = Field(default_factory=dict)


class ApiErrorDetail(SdmModel):
    """The ``error`` object of an SDM error response.

    Attributes:
        code: HTTP status code, for example 400.
        message: Human readable message, for example "Rate limited.".
        status: RPC code, for example ``"FAILED_PRECONDITION"``.

    Source: https://developers.google.com/nest/device-access/reference/errors/api
    """

    code: int
    message: str
    status: str | None = None


class ApiErrorResponse(SdmModel):
    """Top level SDM error body: ``{"error": {...}}``.

    Source: https://developers.google.com/nest/device-access/reference/errors/api
    """

    error: ApiErrorDetail
