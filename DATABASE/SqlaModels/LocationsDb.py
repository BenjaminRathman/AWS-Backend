from sqlalchemy import Column, Integer, String, UUID, ForeignKey
from DATABASE.dbConnection import Base 

class LocationDB(Base):
    __tablename__ = "Locations"

    LocationId = Column(Integer, primary_key=True, index=True)
    LocationName = Column(String, nullable=False)
    
