from fastapi import APIRouter, Depends, HTTPException
from API.Endpoint import verify_token
from API.PydanticModels.UserModels import User
from DATABASE.dbConnection import get_db
from sqlalchemy.orm import Session
from DATABASE.SqlaModels.UsersDb import UserDB

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    #dependencies=[Depends(verify_token)]  
)

@router.post("/createUser")
async def create_user(user: User, db: Session = Depends(get_db)):
    new_user = UserDB(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created", "user_data": user}

