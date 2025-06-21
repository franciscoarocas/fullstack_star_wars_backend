
from typing import Optional, List, Any

from copy import deepcopy



def search(data : List[Any], search_value : Optional[str] = None) -> List[Any]:
  """
  Searches for items in a list of dictionaries based on a search value.
    :param data: The list of dictionaries to search through.
    :param search_value: The value to search for in the 'name' field of each dictionary.
    :return: A list of dictionaries that match the search criteria.
    :raises ValueError: If the search value is empty or None.
  """

  data = deepcopy(data)

  if not search_value or search_value == "":
    return deepcopy(data)

  search_value = search_value.lower().strip()

  found_values = [item for item in data if search_value in item['name'].lower()]

  return found_values