from __future__ import annotations
from pydantic import BaseModel,  Field, ConfigDict


class ChangePassword(BaseModel):
    model_config = ConfigDict(extra='forbid')
    login: str = Field(...)
    token: str = Field(...)
    oldPassword: str = Field(
        ..., alias='oldPassword'
    )
    newPassword: str = Field(
        ..., alias='newPassword'
    )
