from fastapi import APIRouter, Depends
from Endpoint import verify_token
from DATABASE.Models.UserModels import User

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(verify_token)]  
)

@router.post("/createUser")
async def create_user(user: User):
    return {"message": "User created", "user_data": user}