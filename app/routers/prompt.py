
from fastapi import APIRouter, Depends
from app.schemas.prompt import Prompt
from app.services.prompt import PromptService

router = APIRouter()

@router.get("/prompt/", response_model=Prompt)
async def list_people(
    prompt: str,
    svc=Depends(PromptService)
):
    prompt_result = await svc.get_prompt(prompt)
    return Prompt(prompt=prompt, answer=prompt_result)