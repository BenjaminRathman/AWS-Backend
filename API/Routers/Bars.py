from fastapi import APIRouter, Depends, HTTPException
from API.Endpoint import verify_token
from API.PydanticModels.LocationModels import Location, AllBars
from DATABASE.dbConnection import get_db
from sqlalchemy.orm import Session
from DATABASE.SqlaModels.LocationsDb import LocationDB, AllBarsDB
from datetime import datetime, timezone
from uuid import UUID

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

@router.get("/getBar/{BarId}", response_model=AllBars)
async def get_bar(BarId: UUID, db: Session = Depends(get_db)):
    bar = db.query(AllBarsDB).filter(AllBarsDB.BarId == BarId).first()
    if not bar:
        raise HTTPException(status_code=404, detail="Bar not found")
    return bar

@router.get("/allBars", response_model=list[AllBars])
async def get_all_bars(db: Session = Depends(get_db)):
    bars = db.query(AllBarsDB).all()
    return bars

@router.delete("/deleteBar/{BarId}", response_model=AllBars)
async def delete_bar(BarId: UUID, db: Session = Depends(get_db)):
    bar_to_delete = db.query(AllBarsDB).filter(AllBarsDB.BarId == BarId).first()
    if not bar_to_delete:
        raise HTTPException(status_code=404, detail="Bar not found")
    db.delete(bar_to_delete)
    db.commit()
    return bar_to_delete