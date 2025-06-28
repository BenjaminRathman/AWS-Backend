from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional


class AllBars(BaseModel):
    BarId: UUID
    LocationId: int
    BarName: str

    model_config = ConfigDict(from_attributes=True)
    
class AllBarsInfo(BaseModel):
    BarId: UUID
    LocationId: int
    BarName: str
    Description: Optional[str] = None
    WeeklySpecials: Optional[dict[str, str]] = None

    model_config = ConfigDict(from_attributes=True)