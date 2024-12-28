from typing import Generator
from urllib.parse import urlencode

import requests

from .models import MapInfo, SearchMapsParameters, SearchMapsResponse


class TrackmaniaExchange:
    def __init__(self, base_url="https://trackmania.exchange"):
        self.base_url = base_url

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
