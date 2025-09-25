from fastapi import HTTPException, Request
import os
from dotenv import load_dotenv

load_dotenv()

async def verify_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    # TODO: Implement proper JWT token verification
    # For now, this is a placeholder that accepts any token
    token = auth_header.split("Bearer ")[1]
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Placeholder token validation - replace with actual JWT verification
    return {"uid": "placeholder_user", "token": token}
    










