
from app.api.star_wars.base import StarWarsAPIBase

from fastapi import HTTPException

from cachetools import TTLCache, cached

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

    async def get_people(self, *args, **kwargs):
        """
        Fetches people from the SWAPI.
        """

        if 'people' in cache:
            return cache['people']

        try:
          async with httpx.AsyncClient() as client:
              response = await client.get(f"{self.api_url}/people")
              response.raise_for_status()
              parsed_people = self.parse_people_response_data(response.json())
              cache["people"] = parsed_people
              return parsed_people
        except httpx.HTTPStatusError as e:
            logger.error(f"Error fetching people API: {e}")
            raise HTTPException(
                status_code=503,
                detail="Resource temporarily unavailable. Please try again later."
            )


    def parse_planets_response_data(self, data):
        return data


    async def get_planets(self, *args, **kwargs):
        """
        Fetches planets from the SWAPI.
        """

        if 'planets' in cache:
            return cache['planets']

        try:
          async with httpx.AsyncClient() as client:
              response = await client.get(f"{self.api_url}/planets")
              response.raise_for_status()
              parsed_planets = self.parse_planets_response_data(response.json())
              cache["planets"] = parsed_planets
              return parsed_planets
        except httpx.HTTPStatusError as e:
            logger.error(f"Error fetching planets API: {e}")
            raise HTTPException(
                status_code=503,
                detail="Resource temporarily unavailable. Please try again later."
            )