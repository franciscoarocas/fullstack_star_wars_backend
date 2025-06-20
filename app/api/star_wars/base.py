
from abc import ABC, abstractmethod

class StarWarsAPIBase(ABC):

  def __init__(self, api_url : str) -> None:
      self.api_url = api_url

  @abstractmethod
  def parse_people_reponse_data(self, *args, **kwargs):
    pass

  @abstractmethod
  async def get_people(self, *args, **kwargs):
    pass

  @abstractmethod
  def parse_planets_reponse_data(self, *args, **kwargs):
    pass

  @abstractmethod
  async def get_planets(self, *args, **kwargs):
    pass