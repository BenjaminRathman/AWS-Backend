from fastapi import FastAPI
from API.Routers import Users, Health, Locations, Bars

app = FastAPI()
app.include_router(Users.router)
app.include_router(Health.router)
app.include_router(Locations.router)
app.include_router(Bars.router)