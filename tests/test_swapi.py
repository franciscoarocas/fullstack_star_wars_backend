
import pytest

from fastapi import HTTPException

from unittest.mock import MagicMock, patch

from app.api.star_wars.swapi import Swapi, cache

from tests.factory.swapi import (
    build_fake_swapi_people_data,
    build_fake_swapi_planets_data)

from tests.factory.api import (
    build_fake_response,
    build_fake_response_error
)


@pytest.mark.asyncio
@patch("app.api.star_wars.swapi.httpx.Client.get", new_callable=MagicMock)
async def test_get_people(mock_get):
    fake_response = build_fake_swapi_people_data()

    factory = build_fake_response(fake_response)

    mock_get.side_effect = factory
    swapi = Swapi()
    people = await swapi.get_people()

    assert len(people) == 5
    assert people[0]["name"] == "Luke Skywalker"
    assert people[4]["name"] == "Chewbacca"

    # Test that the cache is used
    mock_get.reset_mock() # Deleted fake API call
    people_cached = await swapi.get_people()
    assert people_cached == people



@pytest.mark.asyncio
@patch("app.api.star_wars.swapi.httpx.Client.get", new_callable=MagicMock)
async def test_get_people(mock_get):
    fake_response = build_fake_swapi_people_data()

    factory = build_fake_response(fake_response)

    mock_get.side_effect = factory
    swapi = Swapi()
    people = await swapi.get_people()

    assert len(people) == 5
    assert people[0]["name"] == "Luke Skywalker"
    assert people[4]["name"] == "Chewbacca"

    # Test that the cache is used
    mock_get.reset_mock() # Deleted fake API call
    people_cached = await swapi.get_people()
    assert people_cached == people



@pytest.mark.asyncio
@patch("app.api.star_wars.swapi.httpx.Client.get", new_callable=MagicMock)
async def test_get_people_api_error(mock_get):

    cache.clear()

    factory = build_fake_response_error(status_code=503)
    mock_get.side_effect = factory

    swapi = Swapi()
    with pytest.raises(HTTPException):
        await swapi.get_people()



@pytest.mark.asyncio
@patch("app.api.star_wars.swapi.httpx.Client.get", new_callable=MagicMock)
async def test_get_planets(mock_get):
    fake_response = build_fake_swapi_planets_data()

    factory = build_fake_response(fake_response)

    mock_get.side_effect = factory
    swapi = Swapi()
    planets = await swapi.get_planets()

    assert len(planets) == 5
    assert planets[0]["name"] == "Tatooine"
    assert planets[4]["name"] == "Bespin"
    assert planets[0]["climate"] == "arid"
    assert planets[4]["terrain"] == "gas giant"

    # Test that the cache is used
    mock_get.reset_mock() # Deleted fake API call
    planets_cached = await swapi.get_planets()
    assert planets_cached == planets
