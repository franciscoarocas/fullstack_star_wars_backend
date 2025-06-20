
from fastapi_pagination import Params, paginate


def paginate_func(data, page : int, num_item_per_page : int):
  params = Params(page=page, size=num_item_per_page)
  return paginate(data, params)