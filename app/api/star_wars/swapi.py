
from typing import Callable

from app.api.star_wars.base import StarWarsAPIBase
from app.utils.cache import (
    get_cache,
    set_cache,
    is_in_cache
)

from fastapi import HTTPException

import httpx

import logging


logger = logging.getLogger(__name__)


class Swapi(StarWarsAPIBase):
    """
    Star Wars API client for SWAPI
    """

    __API_URL = "https://swapi.info/api"


    def __init__(self) -> None:
        super().__init__(self.__API_URL)

    def parse_people_response_data(self, data):
        return data

    async def get_people(self):
        """
            Fetches people from the SWAPI.
        """

        return await self.get_api_data('people', self.parse_people_response_data)

    def parse_planets_response_data(self, data):
        return data


    async def get_planets(self):
        """
            Fetches planets from the SWAPI.
        """

        return await self.get_api_data('planets', self.parse_planets_response_data)


    async def get_api_data(self, name : str, parse_func : Callable):
        """
            Fetches data from the SWAPI and caches it.
            If the data is already cached, it returns the cached data.
            Args:
                name (str): The name of the resource (e.g., 'people', 'planets').
                parse_func (Callable): Function to parse the response data.
            Returns:
                Any: Parsed data from the API.
            """
        if await is_in_cache(name):
            return await get_cache(name)

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.api_url}/{name}")
                response.raise_for_status()
                parsed_data = parse_func(response.json())
                await set_cache(name, parsed_data)
                return parsed_data
        except httpx.HTTPStatusError as e:
            logger.error(f"Error fetching {name} API: {e}")
            raise HTTPException(
                status_code=503,
                detail="Resource temporarily unavailable. Please try again later."
            )