"""Shared Pydantic base class for every SDM model.

Python attribute names are snake_case. Each field declares the exact camelCase
JSON key as its alias, so parsing uses ``Model.model_validate(data)`` and
serializing back to the wire uses ``model_dump(by_alias=True)``.
"""

from pydantic import BaseModel, ConfigDict


class SdmModel(BaseModel):
    """Base for all wire models.

    Configuration:
        - ``populate_by_name``: tests and code may build models with snake_case names.
        - ``extra="ignore"``: Google may add fields; unknown keys must not break parsing.
        - ``frozen``: parsed API data is a read only snapshot.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
        frozen=True,
    )
