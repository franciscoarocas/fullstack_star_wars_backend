
import pytest

from app.utils.sorting import sort

def test_sorting_by_name():
  data = [
      {"name": "Bob", "created": "2023-02-01"},
      {"name": "Alice", "created": "2023-01-01"},
      {"name": "Charlie", "created": "2023-03-01"}
  ]

  sorted_by_name_asc = sort(data, sort_by="name", direction="asc")
  assert sorted_by_name_asc == [
      {"name": "Alice", "created": "2023-01-01"},
      {"name": "Bob", "created": "2023-02-01"},
      {"name": "Charlie", "created": "2023-03-01"}
  ]