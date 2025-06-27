from fastapi import APIRouter, Depends
from API.Endpoint import verify_token

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/protected")
async def protected_route(token: dict = Depends(verify_token)):
    return {"message": "Access granted", "token_data": token}

@router.get("/")
def root():
    return {"Hello": "World"}