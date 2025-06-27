from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from uuid import UUID

class User(BaseModel):
    UserId: UUID
    Email: EmailStr
    FirstName: str
    LastName: str
    DateOfBirth: date
    TimeOfLastLogin: datetime
    class Config:
        orm_mode = True