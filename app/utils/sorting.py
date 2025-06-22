
from typing import Optional, List, Any, Callable, Dict
from copy import deepcopy

from fastapi import HTTPException

import logging
from http import HTTPStatus

logger = logging.getLogger(__name__)


class SortStrategy():

  def __init__(self, field : str, sort_func : Callable) -> None:
    """
      SortStrategy class to encapsulate sorting logic.
        :param field: The field to sort by.
        :param sort_func: A callable function that defines the sorting logic.
    """
    self.field = field
    self.__sort_func = sort_func


  def sort(self, data : List[Any]) -> List[Any]:
    """
      Sorts the data based on the defined field and direction.
        :param data: The list of data to sort.
        :return: A sorted list of data.
    """

    return sorted(data, key=self.__sort_func)


SORT_STRATEGIES : Dict[str, SortStrategy] = {
    "name": SortStrategy("name", lambda p: p['name'].lower()),
    "created": SortStrategy("created", lambda p: p['created']),
}


def sort(data : List[Any], sort_by : Optional[str] = None) -> List[Any]:
  """
  Sorts a list of data based on the specified field and direction.
    :param data: The list of data to sort.
    :param sort_by: The field to sort by (e.g., 'name', 'created').
    :param direction: The direction of sorting, either 'asc' or 'desc'.
    :return: A sorted list of data.
    :raises HTTPException: If the sort strategy is not found.
  """

  data = deepcopy(data)

  if not sort_by:
    return data

  sort_strategy = SORT_STRATEGIES.get(sort_by, None)

  if not sort_strategy:
    logger.error(f"Sort strategy '{sort_by}' not found")
    raise HTTPException(
        status_code=HTTPStatus.BAD_REQUEST,
        detail=f"Sort mode '{sort_by}' not found"
    )

  return sort_strategy.sort(data)
