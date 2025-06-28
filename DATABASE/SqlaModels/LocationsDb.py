from sqlalchemy import Column, Integer, String, UUID, ForeignKey
from DATABASE.dbConnection import Base 

class LocationDB(Base):
    __tablename__ = "Locations"

    LocationId = Column(Integer, primary_key=True, index=True)
    LocationName = Column(String, nullable=False)
    
class AllBarsDB(Base):
    __tablename__ = "AllBars"

    BarId = Column(UUID(as_uuid=True), primary_key=True, index=True)
    LocationId = Column(Integer, ForeignKey("Locations.LocationId", ondelete="CASCADE"))
    BarName = Column(String, nullable=False)