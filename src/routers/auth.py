from fastapi import APIRouter
from src.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    # TODO: integrar com users/identity provider
    # mock: emite JWT assinado em outro serviço futuramente
    return {"access_token": "mock", "token_type": "bearer"}