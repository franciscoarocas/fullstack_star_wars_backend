
from typing import Optional
from copy import deepcopy


class SortStrategy():

  def __init__(self, field : str, sort_func : callable):
    self.field = field
    self.__sort_func = sort_func


  def sort(self, data, direction: str = "asc"):

    if direction not in ["asc", "desc"]:
        raise ValueError("Direction must be 'asc' or 'desc'")

    reverse = direction == "desc"

    return sorted(data, key=self.__sort_func, reverse=reverse)


SORT_STRATEGIES = {
    "name": SortStrategy("name", lambda p: p['name'].lower()),
    "created": SortStrategy("created", lambda p: p['created']),
}


def sort(data, sort_by : Optional[str] = None, direction : Optional[str] = 'asc'):

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
