
from typing import Optional

from copy import deepcopy



def search(data, search_value : Optional[str] = None):

  data = deepcopy(data)

  if not search_value or search_value == "":
    return deepcopy(data)

  search_value = search_value.lower().strip()

  found_values = [item for item in data if search_value in item['name'].lower()]

  return found_values