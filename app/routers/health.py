from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
	return {"status": "ok"}

@router.get("/ping", tags=["Health"])
async def ping():
    return {"status": "pong"}