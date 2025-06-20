
from typing import Optional

from app.api.star_wars.builder import stars_wars_api_builder

from fastapi_pagination import Params, paginate

from app.utils.sorting import SORT_STRATEGIES

from copy import deepcopy

import os

NUM_ITEM_PEOPLE = 15

class PeopleService:

  def __init__(self) -> None:
    api_name = os.getenv("STAR_WARS_API", None)
    # TODO: Aquí va otro logger para el getenv
    self.__api = stars_wars_api_builder(api_name)

  @staticmethod
  def __paginate(data, page : int, num_item_per_page : int):
    params = Params(page=page, size=num_item_per_page)
    return paginate(data, params)

  @staticmethod
  def __search(data, search_value : Optional[str] = None):

    data = deepcopy(data)

    if not search_value or search_value == "":
      return deepcopy(data)

    search_value = search_value.lower().strip()

    found_values = [item for item in data if search_value in item['name'].lower()]

    return found_values

  @staticmethod
  def __sort(data, sort_by : Optional[str] = None, direction : Optional[str] = 'asc'):

    data = deepcopy(data)

    if not sort_by:
      return data

    sort_strategy = SORT_STRATEGIES.get(sort_by, None)

    if not direction:
      direction = 'asc'

    if not sort_strategy:
      # TODO: Hacer un logger de error
      return data

    return sort_strategy.sort(data, direction)


  async def get_people(self, page, search, sort, direction):

    people_data = await self.__api.get_people()

    people_data = self.__search(people_data, search)
    people_data = self.__sort(people_data, sort, direction)
    return self.__paginate(people_data, page, NUM_ITEM_PEOPLE)