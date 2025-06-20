
from app.api.star_wars.base import StarWarsAPIBase

import httpx


class Swapi(StarWarsAPIBase):
    """
    Star Wars API client for SWAPI
    """

    __API_URL = "https://swapi.info/api"


    def __init__(self) -> None:
        super().__init__(self.__API_URL)

    def parse_people_reponse_data(self, data):
        return data

    async def get_people(self, *args, **kwargs):
        """
        Fetches people from the SWAPI.
        """

        try:
          async with httpx.AsyncClient() as client:
              response = await client.get(f"{self.api_url}/people")
              response.raise_for_status()
              parsed_people = self.parse_people_reponse_data(response.json())
              return parsed_people
        except httpx.HTTPStatusError as e:
            # TODD: Hacer un manejo de errores más específico
            pass


    def parse_planets_reponse_data(self, data):
        return data


    async def get_planets(self, *args, **kwargs):
        """
        Fetches planets from the SWAPI.
        """

        try:
          async with httpx.AsyncClient() as client:
              response = await client.get(f"{self.api_url}/planets")
              response.raise_for_status()
              parsed_planets = self.parse_planets_reponse_data(response.json())
              return parsed_planets
        except httpx.HTTPStatusError as e:
            # TODD: Hacer un manejo de errores más específico
            pass