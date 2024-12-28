from pydantic import BaseModel, Field


class MapInfo(BaseModel):
    map_id: int = Field(alias="MapId")


class SearchMapsParameters(BaseModel):
    fields: str = "MapId"
    author: str | None = None
    after: int | None = None


class SearchMapsResponse(BaseModel):
    has_more: bool = Field(alias="More")
    results: list[MapInfo] = Field(alias="Results")
