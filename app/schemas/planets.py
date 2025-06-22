
from typing import Optional, Union

from pydantic import BaseModel

from datetime import datetime

class Planet(BaseModel):
  name            : str
  rotation_period : Optional[Union[int | str]] # Rotation period can be a string like "unknown"
  orbital_period  : Optional[Union[int | str]] # Orbital period can be a string like "unknown"
  diameter        : Optional[Union[int | str]] # Diameter can be a string like "unknown"
  climate         : Optional[str]
  gravity         : Optional[str]
  terrain         : Optional[str]
  surface_water   : Optional[Union[int | str]] # Surface water can be a string like "unknown"
  population      : Optional[Union[int | str]] # Population can be a string like "unknown"
  created         : datetime
  edited          : datetime

  class Config:
      json_encoders = {
          datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
      }



class PlanetResponse(BaseModel):
  items : list[Planet]
  total : int
  page  : int
  size  : int
  pages : int