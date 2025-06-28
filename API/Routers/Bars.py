from fastapi import APIRouter, Depends, HTTPException
from API.Endpoint import verify_token
from API.PydanticModels.LocationModels import Location, AllBars
from DATABASE.dbConnection import get_db
from sqlalchemy.orm import Session
from DATABASE.SqlaModels.LocationsDb import LocationDB, AllBarsDB
from datetime import datetime, timezone

router = APIRouter(
    prefix="/bars",
    tags=["Bars"],
    #dependencies=[Depends(verify_token)]  
)

@router.post("/createBar")
async def create_bar(bar: AllBars, db: Session = Depends(get_db)):
    new_bar = AllBarsDB(**bar.model_dump())
    db.add(new_bar)
    db.commit()
    db.refresh(new_bar)
    return new_bar
