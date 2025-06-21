
import pytest

from app.utils.search import search

def build_search_data():
    return [
        {"name": "Bob", "created": "2023-02-01"},
        {"name": "Alice", "created": "2023-01-01"},
        {"name": "Charlie", "created": "2023-03-01"}
    ]

def test_search_with_valid_value():
    data = build_search_data()
    search_value = "Alice"

    found_items = search(data, search_value)

    assert len(found_items) == 1
    assert found_items[0]["name"] == "Alice"


def test_search_with_partial_match():
    data = build_search_data()
    search_value = "lic"

    found_items = search(data, search_value)

    assert len(found_items) == 1
    assert found_items[0]["name"] == "Alice"


def test_search_with_no_match():
    data = build_search_data()
    search_value = "Zoe"

    found_items = search(data, search_value)

    assert len(found_items) == 0


def test_search_with_empty_value():
    data = build_search_data()
    search_value = ""

    found_items = search(data, search_value)

    assert len(found_items) == len(data)
    assert found_items == data


def test_search_with_lowercase_value():
    data = build_search_data()
    search_value = "bob"

    found_items = search(data, search_value)

    assert len(found_items) == 1
    assert found_items[0]["name"] == "Bob"