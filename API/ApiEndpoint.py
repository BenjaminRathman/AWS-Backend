from fastapi import FastAPI, HTTPException, Request, Depends # type: ignore

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}