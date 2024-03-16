from fastapi import FastAPI
from routes.user import user


myapp=FastAPI()
myapp.include_router(user)