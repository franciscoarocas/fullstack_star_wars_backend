
from app.utils.pagination import paginate_func

import pytest

def build_pagination_data():
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
        {"id": 4, "name": "Item 4"},
        {"id": 5, "name": "Item 5"},
        {"id": 6, "name": "Item 6"},
        {"id": 7, "name": "Item 7"},
        {"id": 8, "name": "Item 8"},
        {"id": 9, "name": "Item 9"},
        {"id": 10, "name": "Item 10"}
    ]


def test_paginate_with_valid_page_and_size():

    data = build_pagination_data()
    page = 1
    num_item_per_page = 5

    paginated_data = paginate_func(data, page, num_item_per_page)

    print(paginated_data)

    assert paginated_data.total == 10
    assert paginated_data.page == 1
    assert paginated_data.size == 5
    assert paginated_data.pages == 2
    assert paginated_data.items[0]["id"] == 1
    assert paginated_data.items[2]["id"] == 3
    assert paginated_data.items[4]["id"] == 5


def test_paginate_with_invalid_page():
    data = build_pagination_data()
    page = 3  # This page does not exist with 5 items per page
    num_item_per_page = 5

    paginated_data = paginate_func(data, page, num_item_per_page)

    assert paginated_data.total == 10
    assert paginated_data.page == 3
    assert paginated_data.size == 5
    assert paginated_data.pages == 2
    assert len(paginated_data.items) == 0  # No items on this page