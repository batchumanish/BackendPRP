from fastapi import APIRouter,Query
from models.user import User 
from config.db import conn 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter() 
# db = conn["manishclouddb"]
# restaurants_collection = db["testcollection"]


@user.get('/get_test_data')
async def get_test_collection_data():
    return serializeList(conn.manishclouddb.testcollection.find())

@user.get("/search_restaurant/")
async def search_restaurant(
    restaurant_name: str ,
    menu_item_name: str
):
    query = {}
    if restaurant_name:
        query["$or"] = [{"name": {"$regex": f".*{restaurant_name}.*", "$options": "i"}}]
    if menu_item_name:
        query["$or"].append({"menu.name": {"$regex": f".*{menu_item_name}.*", "$options": "i"}}) if "$or" in query else query.update({"menu.name": {"$regex": f".*{menu_item_name}.*", "$options": "i"}})

    pipeline = [
        {"$match": query},
        {"$unwind": "$menu"},
        {"$match": query}
    ]

    result = serializeList(conn.manishclouddb.testcollection.aggregate(pipeline))


    return {"results":result}

