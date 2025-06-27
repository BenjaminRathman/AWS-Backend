from fastapi import FastAPI
from API.Routers import Users, Health

app = FastAPI()
app.include_router(Users.router)
app.include_router(Health.router)