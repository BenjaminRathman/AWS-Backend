from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date, datetime
from uuid import UUID

class User(BaseModel):
    UserId: UUID
    Email: EmailStr
    FirstName: str
    LastName: str
    DateOfBirth: date
    TimeOfLastLogin: datetime
    model_config = ConfigDict(from_attributes=True)