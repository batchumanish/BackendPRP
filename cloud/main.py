from fastapi import FastAPI
from pymongo import MongoClient

client=MongoClient('mongodb+srv://manishbatchu:Q7h5KtERcGZdfJ4E@manishcluster.71tedsw.mongodb.net/')

db=client.get_database('manishclouddb')

records=db.restdata

print(records.count_documents({}))
# Initialize FastAPI app
user = FastAPI()



@user.get("/data")
async def get_data():
    data =records.count_documents({})

    if data:
        return {"status": "success", "data": data}
    else:
        return {"status": "error", "message": "Data not found"}
