import pytest
from unittest.mock import patch, MagicMock

import httpx
from fastapi import status
from app.main import app
from tests.factory.swapi import (
    build_fake_swapi_people_data,
    build_fake_swapi_planets_data
)
from tests.factory.api import build_fake_response

from app.utils.ia_common import ANSWER_QUESTIONS


@pytest.mark.asyncio
@patch("app.api.star_wars.swapi.httpx.Client.get", new_callable=MagicMock)
async def test_people_endpoint(mock_get):

    mock_get.side_effect = build_fake_response(build_fake_swapi_people_data())

    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/people/")

    assert res.status_code == status.HTTP_200_OK
    assert res.json()["items"][0]["name"] == "Luke Skywalker"




@pytest.mark.asyncio
async def test_planets_endpoint(monkeypatch):
    fake_data = build_fake_swapi_planets_data()

    async def fake_get(self, url, *args, **kwargs) -> httpx.Response:
        return httpx.Response(status_code=200, json=fake_data)

    monkeypatch.setattr(
        "app.api.star_wars.swapi.httpx.AsyncClient.get",
        fake_get,
        raising=True,
    )

    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/planets/")

    assert res.status_code == status.HTTP_200_OK
    assert res.json() == fake_data


@pytest.mark.asyncio
async def test_prompt_endpoint():

    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/prompt/", params={"prompt": "give me and example of planet"})

    assert res.status_code == status.HTTP_200_OK
    assert res.json()["prompt"] in "give me and example of planet"

    found = False
    for planet in ANSWER_QUESTIONS['planet']:
        if planet in res.json()["answer"]:
            found = True
            break
    assert found == True, "Expected planet name not found in the answer"


@pytest.mark.asyncio
async def test_prompt_endpoint_invalid():

    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/prompt/", params={"prompt": "give me and example of something"})

    assert res.status_code == status.HTTP_200_OK
    assert res.json()["prompt"] in "give me and example of something"
    assert res.json()["answer"] == "I don't know how to answer that question."