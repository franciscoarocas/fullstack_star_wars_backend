

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