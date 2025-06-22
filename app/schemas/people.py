
from pydantic import BaseModel

from typing import Optional, Union

from datetime import datetime

class People(BaseModel):
  name       : str
  height     : Optional[Union[int | str]] # Height can be a string like "unknown"
  mass       : Optional[Union[int | str]] # Mass can be a string like "unknown"
  hair_color : Optional[str]
  skin_color : Optional[str]
  eye_color  : Optional[str]
  birth_year : Optional[str]
  gender     : Optional[str]
  created    : datetime
  edited     : datetime

  class Config:
      json_encoders = {
          datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
      }


class PeopleResponse(BaseModel):
  items : list[People]
  total : int
  page  : int
  size  : int
  pages : int