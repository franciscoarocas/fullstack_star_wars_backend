
from .people import router as people_router
from .planets import router as planets_router
from .prompt import router as prompt_router

all_routes = [
  people_router,
  planets_router,
  prompt_router
]