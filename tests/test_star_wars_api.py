
import pytest

from app.api.star_wars.builder import (
  stars_wars_api_builder,
  get_star_wars_api_from_env
)
from app.api.star_wars.swapi import Swapi
from fastapi import HTTPException

def test_star_wars_api_builder(caplog):

    # Test valid API name
    api_instance = stars_wars_api_builder("swapi")
    assert isinstance(api_instance, Swapi)

    # Test invalid API name
    with caplog.at_level("CRITICAL"):
      with pytest.raises(HTTPException) as exc_info:
          stars_wars_api_builder("invalid_api")

    assert exc_info.value.status_code == 503
    assert "Resource temporarily unavailable" in str(exc_info.value.detail)



def test_start_wars_api_from_env(monkeypatch, caplog):

    # Test with valid environment variable
    monkeypatch.setenv("STAR_WARS_API", "swapi")
    api_instance = get_star_wars_api_from_env()
    assert isinstance(api_instance, Swapi)

    # Test with invalid environment variable
    monkeypatch.setenv("STAR_WARS_API", "invalid_api")
    with pytest.raises(HTTPException) as exc_info:
        get_star_wars_api_from_env()

    assert exc_info.value.status_code == 503
    assert "Resource temporarily unavailable" in str(exc_info.value.detail)

    # Test with no environment variable set
    monkeypatch.delenv("STAR_WARS_API", raising=False)
    with caplog.at_level("WARNING"):
        api_instance = get_star_wars_api_from_env()
    assert isinstance(api_instance, Swapi)