
from typing import List, Any

from fastapi_pagination import Params, paginate

def paginate_func(data : List[Any], page : int, num_item_per_page : int) -> List[Any]:
  """
  Paginates a list of data based on the specified page number and number of items per page.
    :param data: The list of data to paginate.
    :param page: The page number to retrieve.
    :param num_item_per_page: The number of items per page.
    :return: A paginated list of data.
  """
  params = Params(page=page, size=num_item_per_page)
  return paginate(data, params)