
from typing import List

from fastapi import APIRouter, Query, Depends
from app.schemas.people import PeopleResponse
from app.services.people import PeopleService

router = APIRouter()

@router.get("/people/", response_model=PeopleResponse)
async def list_people(
    page: int = Query(1, ge=1),
    search: str | None = Query(None),
    sort: str | None = Query(None),
    dir: str | None = Query(None),
    svc=Depends(PeopleService)
):
    results = await svc.get_people(page, search, sort, dir)
    return results