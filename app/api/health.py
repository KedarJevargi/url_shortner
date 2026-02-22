from fastapi import APIRouter


router = APIRouter(prefix="/health",tags=["Health"])


@router.get(path="", tags=["health"])
async def health_check():
    return {"Status":"Ok"}


