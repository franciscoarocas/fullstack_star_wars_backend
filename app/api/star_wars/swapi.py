
from app.api.star_wars.base import StarWarsAPIBase

import httpx


class Swapi(StarWarsAPIBase):
    """
    Star Wars API client for SWAPI
    """

    __API_URL = "https://swapi.info/api"


    def __init__(self) -> None:
        super().__init__(self.__API_URL)


    def filter_people(self, data, *args, **kwargs):
        return data


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
              filtered_people = self.filter_people(parsed_people, *args)
              return filtered_people
        except httpx.HTTPStatusError as e:
            # TODD: Hacer un manejo de errores más específico
            pass
