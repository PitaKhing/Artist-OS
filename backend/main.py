from fastapi import FastAPI
from routes.releases import router as releases_router
from database import engine, Base
import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(releases_router)


@app.get("/")
def home():
    return {"message": "ArtistOS API is running"}


