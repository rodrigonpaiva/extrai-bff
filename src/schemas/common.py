from pydantic import BaseModel
from typing import List


class DailyCount(BaseModel):
    date: str
    count: int


class TopMember(BaseModel):
    memberId: str
    messages: int


class GroupOverview(BaseModel):
    messagesPerDay: List[DailyCount]
    activeUsers: int
    topMembers: List[TopMember]
