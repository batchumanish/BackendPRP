from fastapi import APIRouter
from models.user import User 
from config.db import conn 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter() 

@user.get('/get_data')
async def find_all_users():
    return serializeList(conn.manishclouddb.restdata.find())

