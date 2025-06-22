
from typing import Optional

from app.api.star_wars.builder import get_star_wars_api_from_env

from app.utils.sorting import sort as sort_func
from app.utils.search import search as search_func
from app.utils.pagination import paginate_func

from app.constants import NUM_ITEMS_TABLE_PAGE


class PlanetsService:

  def __init__(self) -> None:
    self.__api = get_star_wars_api_from_env()

  async def get_planets(self, page : int, search : Optional[str], sort : Optional[str], direction : Optional[str]) -> dict:
    """
    Fetches planets data, applies search, sorting, and pagination.
    Args:
        page (int): The page number for pagination.
        search (str | None): Search term to filter planets.
        sort (str | None): Field to sort the planets by.
        direction (str | None): Direction of sorting ('asc' or 'desc').
    Returns:
        dict: Paginated and sorted planets data.
    """

    planets_data = await self.__api.get_planets()

    planets_data = search_func(planets_data, search)
    planets_data = sort_func(planets_data, sort, direction)
    return paginate_func(planets_data, page, NUM_ITEMS_TABLE_PAGE)