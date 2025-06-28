from pydantic import BaseModel, ConfigDict

class Location(BaseModel):
    LocationId: int
    LocationName: str

    model_config = ConfigDict(from_attributes=True)
    