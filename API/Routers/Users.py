from fastapi import APIRouter, Depends, HTTPException
from API.Endpoint import verify_token
from API.PydanticModels.UserModels import User
from DATABASE.dbConnection import get_db
from sqlalchemy.orm import Session
from DATABASE.SqlaModels.UsersDb import UserDB
from datetime import datetime, timezone

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    #dependencies=[Depends(verify_token)]  
)

@router.post("/createUser")
async def create_user(user: User, db: Session = Depends(get_db)):
    new_user = UserDB(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/getUser/{UserId}", response_model=User)
async def get_user(UserId: str, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.UserId == UserId).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/updateUserLastLogin/{UserId}", response_model=User)
async def update_user(UserId: str, db: Session = Depends(get_db)):
    user_to_update = db.query(UserDB).filter(UserDB.UserId == UserId).first()
    if not user_to_update:
        raise HTTPException(status_code=404, detail="User not found")
    user_to_update.TimeOfLastLogin = datetime.now(timezone.utc)
    db.commit()
    db.refresh(user_to_update)
    return user_to_update

@router.delete("/deleteUser/{UserId}", response_model=User)
async def delete_user(UserId: str, db: Session = Depends(get_db)):
    user_to_delete = db.query(UserDB).filter(UserDB.UserId == UserId).first()
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user_to_delete)
    db.commit()
    return user_to_delete