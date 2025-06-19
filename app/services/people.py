
from app.api.star_wars.builder import stars_wars_api_builder

import os

class PeopleService:

  def __init__(self) -> None:
    api_name = os.getenv("STAR_WARS_API", "swapi")
    self.__api = stars_wars_api_builder(api_name)


  async def get_people(self, **kwargs):
    return await self.__api.get_people()