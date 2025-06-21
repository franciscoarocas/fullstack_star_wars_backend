
from typing import Callable

from app.api.star_wars.base import StarWarsAPIBase

from fastapi import HTTPException

from cachetools import TTLCache

import httpx

import logging

logger = logging.getLogger(__name__)

cache = TTLCache(maxsize=1024, ttl=60)

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

        return self.get_api_data('people', self.parse_people_response_data)

    def parse_planets_response_data(self, data):
        return data


    async def get_planets(self):
        """
            Fetches planets from the SWAPI.
        """

        return self.get_api_data('planets', self.parse_planets_response_data)


    def get_api_data(self, name : str, parse_func : Callable):
        """
        Generic method to fetch data from the SWAPI.
        :param name: The name of the resource (e.g., 'people', 'planets').
        :param parse_func: Function to parse the response data.
        :return: Parsed data from the API.
        """
        if name in cache:
            return cache[name]

        try:
            with httpx.Client() as client:
                response = client.get(f"{self.api_url}/{name}")
                response.raise_for_status()
                parsed_data = parse_func(response.json())
                cache[name] = parsed_data
                return parsed_data
        except httpx.HTTPStatusError as e:
            logger.error(f"Error fetching {name} API: {e}")
            raise HTTPException(
                status_code=503,
                detail="Resource temporarily unavailable. Please try again later."
            )