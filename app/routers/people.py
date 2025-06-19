
from typing import List

from fastapi import APIRouter, Query, Depends
from app.schemas.people import People
from app.services.people import PeopleService

router = APIRouter()

@router.get("/")
async def list_people(
    page: int = Query(1, ge=1),
    search: str | None = Query(None),
    sort: str | None = Query("name"),
    dir: str | None = Query("asc"),
    response_model=List[People],
    svc=Depends(PeopleService)
):
    results = await svc.get_people(page=page, search=search, sort=sort, dir=dir)
    return results
    #return PeopleService.from_results(results, page)