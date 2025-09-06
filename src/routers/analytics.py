from fastapi import APIRouter, Depends
from src.core.security import require_jwt
from src.schemas.analytics import GroupOverview

router = APIRouter()

@router.get("/groups/{group_id}/overview", response_model=GroupOverview)
def group_overview(group_id: str, _user=Depends(require_jwt)):
    # TODO: consultar agregações reais no Postgres
    return {
        "messagesPerDay": [{"date": "2025-09-01", "count": 42}],
        "activeUsers": 12,
        "topMembers": [{"memberId": "u1", "messages": 10}],
    }