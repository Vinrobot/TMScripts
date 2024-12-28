from typing import Final, Literal

from pydantic import BaseModel, Field

MAP_INFO_FIELDS: Final = [
    "MapId",
    "MapUid",
    "GbxMapName",
    "Name",
    "Authors",
    "Tags",
]

MAP_INFO_FIELDS_STR: Final = ",".join(MAP_INFO_FIELDS)


class MapTag(BaseModel):
    id: int = Field(alias="TagId")
    name: str = Field(alias="Name")
    color: str = Field(alias="Color")


class MapUser(BaseModel):
    id: int = Field(alias="UserId")
    name: str = Field(alias="Name")


class MapAuthor(BaseModel):
    user: MapUser = Field(alias="User")
    role: str = Field(alias="Role")


class MapInfo(BaseModel):
    map_id: int = Field(alias="MapId")
    map_uid: str = Field(alias="MapUid")
    gbx_map_name: str = Field(alias="GbxMapName")
    name: str = Field(alias="Name")
    authors: list[MapAuthor] = Field(alias="Authors")
    tags: list[MapTag] = Field(alias="Tags")


class SearchMapsParameters(BaseModel):
    fields: str = MAP_INFO_FIELDS_STR
    order1: int | None = None
    order2: int | None = None
    count: Literal[100] = 100
    after: int | None = None
    before: int | None = None
    name: str | None = None
    author: str | None = None
    author_id: int | None = Field(alias="authoruserid", default=None)


class SearchMapsResponse(BaseModel):
    has_more: bool = Field(alias="More")
    results: list[MapInfo] = Field(alias="Results")
