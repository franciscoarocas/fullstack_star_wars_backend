
from .people import router as people_router
from .planets import router as planets_router

all_routes = [
  people_router,
  planets_router
]