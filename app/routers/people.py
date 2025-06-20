
from typing import List

from fastapi import APIRouter, Query, Depends
from app.schemas.people import People
from app.services.people import PeopleService

router = APIRouter()

@router.get("/people/")
async def list_people(
    page: int = Query(1, ge=1),
    search: str | None = Query(None),
    sort: str | None = Query(None),
    dir: str | None = Query(None),
    response_model=List[People],
    svc=Depends(PeopleService)
):
    results = await svc.get_people(page, search, sort, dir)
    return results