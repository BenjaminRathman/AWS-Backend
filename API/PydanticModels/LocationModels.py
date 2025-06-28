from pydantic import BaseModel, ConfigDict
from uuid import UUID

class Location(BaseModel):
    LocationId: int
    LocationName: str

    model_config = ConfigDict(from_attributes=True)
    