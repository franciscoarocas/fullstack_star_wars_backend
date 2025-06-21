
from app.api.star_wars.base import StarWarsAPIBase

from fastapi import HTTPException

import os

import logging


logger = logging.getLogger(__name__)


def stars_wars_api_builder(api_name : str) -> StarWarsAPIBase:
    """
    Factory function to create an instance of a Star Wars API client.
    Args:
        api_name (str): The name of the API to instantiate.
    Returns:
        StarWarsAPIBase: An instance of the specified Star Wars API client.
    """

    if api_name == "swapi":
        from app.api.star_wars.swapi import Swapi
        return Swapi()

    logger.critical(f"Unknown API name: {api_name}")

    raise HTTPException(
        status_code=503,
        detail="Resource temporarily unavailable. Please try again later."
    )



def get_star_wars_api_from_env() -> StarWarsAPIBase:
    """
    Get the Star Wars API client based on the environment variable.
    Returns:
        StarWarsAPIBase: An instance of the specified Star Wars API client.
    """

    api_name = os.getenv("STAR_WARS_API", "swapi")

    if not api_name:
        logger.warning("STAR_WARS_API environment variable is not set.")

    return stars_wars_api_builder(api_name)