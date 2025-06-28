from sqlalchemy import Column, Integer, String, UUID, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from DATABASE.dbConnection import Base 

class AllBarsDB(Base):
    __tablename__ = "AllBars"

    BarId = Column(UUID(as_uuid=True), primary_key=True, index=True)
    LocationId = Column(Integer, ForeignKey("Locations.LocationId", ondelete="CASCADE"))
    BarName = Column(String, nullable=False)
    
class AllBarsInfoDB(Base):
    __tablename__ = "AllBarsInfo"

    BarId = Column(UUID(as_uuid=True), primary_key=True)
    LocationId = Column(Integer, ForeignKey("Locations.LocationId"), nullable=False)
    BarName = Column(String, nullable=False)
    Description = Column(String, nullable=True)
    WeeklySpecials = Column(JSONB, nullable=True)