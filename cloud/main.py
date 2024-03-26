import motor
from beanie import init_beanie
from fastapi import FastAPI
from routes.user import user
from pydantic import BaseSettings


app=FastAPI()
# app.include_router(user)
from models.user import Gg


class Settings(BaseSettings):
    # mongo_host: str = "localhost"
    # mongo_user: str = "beanie"
    # mongo_pass: str = "beanie"
    # mongo_db: str = "beanie_db"

    @property
    def mongo_dsn(self):
        return f"mongodb+srv://manishbatchu:Q7h5KtERcGZdfJ4E@manishcluster.71tedsw.mongodb.net/"


@app.on_event("startup")
async def app_init():
    # CREATE MOTOR CLIENT
    client = motor.motor_asyncio.AsyncIOMotorClient(
        Settings().mongo_dsn
    )

    # INIT BEANIE
    await init_beanie(client.beanie_db, document_models=[Gg])

    # ADD ROUTES
    app.include_router(user, prefix="/v1", tags=["notes"])

