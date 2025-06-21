import pytest
from unittest.mock import patch, MagicMock

import httpx
from fastapi import status
from app.main import app
from tests.factory.swapi import build_fake_swapi_people_data
from tests.factory.api import build_fake_response


@pytest.mark.asyncio
@patch("app.api.star_wars.swapi.httpx.Client.get", new_callable=MagicMock)
async def test_people_endpoint(mock_get):
    # fuerza ejecución real del servicio (opcional si hay caché)

    # mock de la llamada a la API externa
    mock_get.side_effect = build_fake_response(build_fake_swapi_people_data())

    # transport ASGI que ejecuta la app en el MISMO hilo
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/people/")

    assert res.status_code == status.HTTP_200_OK
    assert res.json()["items"][0]["name"] == "Luke Skywalker"
