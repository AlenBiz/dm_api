from __future__ import annotations
from pydantic import BaseModel,  Field, ConfigDict


class ChangePassword(BaseModel):
    model_config = ConfigDict(extra='forbid')

    login: str = Field(...)
    token: str = Field(...)
    oldPassword: str = Field(
        ..., serialization_alias='old_password'
    )
    newPassword: str = Field(
        ..., serialization_alias='new_password'
    )
