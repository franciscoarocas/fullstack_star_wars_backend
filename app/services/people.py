
from app.api.star_wars.builder import get_star_wars_api_from_env

from app.utils.sorting import sort as sort_func
from app.utils.search import search as search_func
from app.utils.pagination import paginate_func
from app.constants import NUM_ITEMS_TABLE_PAGE


class PeopleService:

  def __init__(self) -> None:
    self.__api = get_star_wars_api_from_env()

  async def get_people(self, page, search, sort, direction):

    people_data = await self.__api.get_people()

    people_data = search_func(people_data, search)
    people_data = sort_func(people_data, sort, direction)
    return paginate_func(people_data, page, NUM_ITEMS_TABLE_PAGE)