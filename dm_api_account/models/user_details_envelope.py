from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import List, Any, Optional

from pydantic import BaseModel, ConfigDict, Field

from dm_api_account.models.user_envelope import UserRole, Rating


class UserDetailsEnvelope(BaseModel):
    model_config = ConfigDict(extra='forbid')
    resource: Optional[UserDetails] = None
    metadata: Optional[Any] = None


class UserDetails(BaseModel):
    model_config = ConfigDict(extra='forbid')
    login: str = Field(None, description='Login')
    roles: List[UserRole]
    medium_picture_url: str = Field(None, alias='mediumPictureUrl')
    small_picture_url: str = Field(None, alias='smallPictureUrl')
    status: str = Field(None)
    rating: Rating
    online: datetime = Field(None)
    name: str = Field(None)
    location: str = Field(None)
    registration: datetime = Field(None)
    icq: str = Field(None)
    skype: str = Field(None)
    original_picture_url: str = Field(None, alias='originalPictureUrl')
    info: Any = Field(None)
    settings: UserSettings = None


class UserSettings(BaseModel):
    model_config = ConfigDict(extra='forbid')
    color_schema: ColorSchema = Field(None, alias='colorSchema')
    nanny_greetings_message: str = Field(None, alias='nannyGreetingsMessage')
    paging: PagingSettings = None


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class PagingSettings(BaseModel):
    model_config = ConfigDict(extra='forbid')
    posts_per_page: int = Field(None, alias='postsPerPage')
    comments_per_page: int = Field(None, alias='commentsPerPage')
    topics_per_page: int = Field(None, alias='topicsPerPage')
    messages_per_page: int = Field(None, alias='messagesPerPage')
    entities_per_page: int = Field(None, alias='entitiesPerPage')