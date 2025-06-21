
import pytest

from fastapi import HTTPException

from app.utils.sorting import sort


def build_data():
    return [
        {"name": "Bob", "created": "2023-02-01"},
        {"name": "Alice", "created": "2023-01-01"},
        {"name": "Charlie", "created": "2023-03-01"}
    ]

def test_sorting_by_name():
  data = build_data()

  sorted_by_name_asc = sort(data, sort_by="name", direction="asc")
  assert sorted_by_name_asc == [
      {"name": "Alice", "created": "2023-01-01"},
      {"name": "Bob", "created": "2023-02-01"},
      {"name": "Charlie", "created": "2023-03-01"}
  ]


def test_sorting_without_direction():
  data = build_data()

  sorted_by_name_desc = sort(data, sort_by="name", direction=None)
  assert sorted_by_name_desc == [
      {"name": "Alice", "created": "2023-01-01"},
      {"name": "Bob", "created": "2023-02-01"},
      {"name": "Charlie", "created": "2023-03-01"}
  ]


def test_sorting_by_desc():
  data = build_data()

  sorted_by_name_desc = sort(data, sort_by="name", direction="desc")
  assert sorted_by_name_desc == [
      {"name": "Charlie", "created": "2023-03-01"},
      {"name": "Bob", "created": "2023-02-01"},
      {"name": "Alice", "created": "2023-01-01"}
  ]


def test_unknown_sorting_type():
  data = build_data()

  with pytest.raises(HTTPException):
      sort(data, sort_by="unknown_field", direction="asc")


def test_no_sorting():
    data = build_data()

    sorted_data = sort(data, sort_by=None, direction=None)
    assert sorted_data == data


def test_invalid_direction():
    data = build_data()

    with pytest.raises(HTTPException):
        sort(data, sort_by="name", direction="invalid_direction")