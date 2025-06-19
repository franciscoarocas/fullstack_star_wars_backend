
from app.api.star_wars.base import StarWarsAPIBase



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

    # TODO: Esto va para el logger
    raise ValueError(f"Unknown API name: {api_name}")