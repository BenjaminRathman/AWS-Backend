from fastapi import APIRouter, Depends, HTTPException
from API.Endpoint import verify_token
from API.PydanticModels.BarsModels import AllBars, AllBarsInfo
from DATABASE.dbConnection import get_db
from sqlalchemy.orm import Session
from DATABASE.SqlaModels.BarsDb import AllBarsDB, AllBarsInfoDB
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

#AllBarInfo

@router.post("/createBarInfo")
async def create_bar_info(bar_info: AllBarsInfo, db: Session = Depends(get_db)):
    new_bar_info = AllBarsInfoDB(**bar_info.model_dump())
    db.add(new_bar_info)
    db.commit()
    db.refresh(new_bar_info)
    return new_bar_info

@router.get("/getBarInfo/{BarId}", response_model=AllBarsInfo)
async def get_bar_info(BarId: UUID, db: Session = Depends(get_db)):
    bar_info = db.query(AllBarsInfoDB).filter(AllBarsInfoDB.BarId == BarId).first()
    if not bar_info:
        raise HTTPException(status_code=404, detail="Bar info not found")
    return bar_info

@router.get("/allBarInfo", response_model=list[AllBarsInfo])
async def get_all_bar_info(db: Session = Depends(get_db)):
    bar_info = db.query(AllBarsInfoDB).all()
    return bar_info

@router.put("/updateBarInfo/{BarId}", response_model=AllBarsInfo)
async def update_bar_info(BarId: UUID, bar_info: AllBarsInfo, db: Session = Depends(get_db)):
    bar_info_to_update = db.query(AllBarsInfoDB).filter(AllBarsInfoDB.BarId == BarId).first()
    if not bar_info_to_update:
        raise HTTPException(status_code=404, detail="Bar info not found")
    
    bar_info_to_update.WeeklySpecials = bar_info.WeeklySpecials
    db.commit()
    db.refresh(bar_info_to_update)
    return bar_info_to_update


@router.delete("/deleteBarInfo/{BarId}", response_model=AllBarsInfo)
async def delete_bar_info(BarId: UUID, db: Session = Depends(get_db)):
    bar_info_to_delete = db.query(AllBarsInfoDB).filter(AllBarsInfoDB.BarId == BarId).first()
    if not bar_info_to_delete:
        raise HTTPException(status_code=404, detail="Bar info not found")
    db.delete(bar_info_to_delete)
    db.commit()
    return bar_info_to_delete