from fastapi import FastAPI
from API.Routers import Users, Health, Locations

app = FastAPI()
app.include_router(Users.router)
app.include_router(Health.router)
app.include_router(Locations.router)