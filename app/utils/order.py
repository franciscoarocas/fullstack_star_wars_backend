
from typing import List, Any, Optional

from fastapi import HTTPException

from http import HTTPStatus

from copy import deepcopy

import logging

logger = logging.getLogger(__name__)

def order_by(data : List[Any], direction : Optional[str] = 'asc') -> List[Any]:
  """
    Orders a list of data in ascending or descending order.
      :param data: The list of data to order.
      :param direction: The direction of ordering, either 'asc' or 'desc'.
      :return: An ordered list of data.
      :raises HTTPException: If the direction is not 'asc' or 'desc'.
  """

  data = deepcopy(data)

  if not direction or direction == 'asc':
    return data

  if direction == 'desc':
    list.reverse(data)
    return data

  logger.error(f"Invalid direction '{direction}' specified for ordering")

  raise HTTPException(
    status_code=HTTPStatus.BAD_REQUEST,
    detail="Direction must be 'asc' or 'desc'"
  )
