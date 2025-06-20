
from typing import List

from fastapi import APIRouter, Query, Depends
from app.schemas.people import People # TODO: CAmbiar este people por Planet
from app.services.planets import PlanetsService

router = APIRouter()

@router.get("/planets/")
async def list_planets(
    page: int = Query(1, ge=1),
    search: str | None = Query(None),
    sort: str | None = Query(None),
    dir: str | None = Query(None),
    response_model=List[People],
    svc=Depends(PlanetsService)
):
    results = await svc.get_planets(page, search, sort, dir)
    return results