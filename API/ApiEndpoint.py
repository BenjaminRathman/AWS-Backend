from fastapi import FastAPI, HTTPException, Request, Depends # type: ignore
import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv
from pathlib import Path


app = FastAPI()

load_dotenv()
base_dir = Path(__file__).resolve().parent
relative_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
firebase_creds_path = (base_dir / relative_path).resolve()
cred = credentials.Certificate(firebase_creds_path)
firebase_admin.initialize_app(cred)

async def verify_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    id_token = auth_header.split("Bearer ")[1]
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
@app.get("/protected")
async def protected_route(token: dict = Depends(verify_token)):
    return {"message": "Access granted", "token_data": token}

@app.get("/")
def root():
    return {"Hello": "World"}


#impement router for the api







