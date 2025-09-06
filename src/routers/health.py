from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Readiness/Liveness")
def health():
    return {"status": "ok"}
