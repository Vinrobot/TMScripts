from os import PathLike
from typing import Generator
from urllib.parse import urlencode

import requests

from .models import MapInfo, SearchMapsParameters, SearchMapsResponse


def download(url: str, path: str | bytes | PathLike, chunk_size=8192):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(path, "wb+") as fp:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                fp.write(chunk)


class TrackmaniaExchange:
    def __init__(self, base_url="https://trackmania.exchange"):
        self.base_url = base_url

    def download_map(self, path: str | bytes | PathLike, map_id: int, shortName: str | None = None):
        url = f"{self.base_url}/maps/download/{map_id}"
        if shortName:
            url += "/" + shortName
        download(url, path)

    def search_maps(self, params: SearchMapsParameters) -> Generator[MapInfo, None, None]:
        params = params.model_copy()

        while True:
            encoded_params = urlencode(params.model_dump(exclude_none=True))
            response = requests.get(f"{self.base_url}/api/maps?{encoded_params}")
            response.raise_for_status()
            page = SearchMapsResponse(**response.json())

            yield from page.results

            if not page.has_more:
                return

            params.after = page.results[-1].map_id
