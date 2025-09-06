from fastapi import APIRouter, Depends
from src.core.security import require_jwt

router = APIRouter()

@router.get("/", summary="List groups")
def list_groups(_user=Depends(require_jwt)):
    return [{"id": "g1", "name": "Grupo 1"}, {"id": "g2", "name": "Grupo 2"}]