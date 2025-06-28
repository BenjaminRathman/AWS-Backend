from fastapi import APIRouter, Depends, HTTPException
from API.Endpoint import verify_token
from API.PydanticModels.LocationModels import Location, AllBars
from DATABASE.dbConnection import get_db
from sqlalchemy.orm import Session
from DATABASE.SqlaModels.LocationsDb import LocationDB, AllBarsDB
from datetime import datetime, timezone

router = APIRouter(
    prefix="/locations",
    tags=["Locations"],
    #dependencies=[Depends(verify_token)]  
)

#Locations

@router.post("/createLocation")
async def create_location(location: Location, db: Session = Depends(get_db)):
    new_location = LocationDB(**location.model_dump())
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location

@router.get("/getLocation/{LocationId}", response_model=Location)
async def get_location(LocationId: int, db: Session = Depends(get_db)):
    location = db.query(LocationDB).filter(LocationDB.LocationId == LocationId).first()
    print(location)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.get("/allLocations", response_model=list[Location]) #not tested yet
async def get_all_locations(db: Session = Depends(get_db)):
    locations = db.query(LocationDB).all()
    return locations

@router.put("/updateLocation/{LocationId}", response_model=Location)
async def update_location(LocationId: int, location: Location, db: Session = Depends(get_db)):
    location_to_update = db.query(LocationDB).filter(LocationDB.LocationId == LocationId).first()
    if not location_to_update:
        raise HTTPException(status_code=404, detail="Location not found")
    location_to_update.LocationName = location.LocationName
    db.commit()
    db.refresh(location_to_update)
    return location_to_update

@router.delete("/deleteLocation/{LocationId}", response_model=Location)
async def delete_location(LocationId: int, db: Session = Depends(get_db)):
    location_to_delete = db.query(LocationDB).filter(LocationDB.LocationId == LocationId).first()
    if not location_to_delete:
        raise HTTPException(status_code=404, detail="Location not found")
    db.delete(location_to_delete)
    db.commit()
    return location_to_delete