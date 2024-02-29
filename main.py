from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
import json
import requests
from typing import List, Optional

app=FastAPI()

file_path="database.json" 


def read_data():
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def write_data(data):
    with open(file_path, "w") as file:
        json.dump(data, file,indent = 4)

@app.get("/get_data")
async def get_data():
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

# @app.post("/data")
# async def add_data(new_data: dict):
#     current_data = read_data() #gets the data in json
#     current_data.update(new_data)# adds or update the json
#     write_data(current_data)
#     return {"message": "Data added successfully"}


# @app.post("/add_value")
# async def add_value(new_value: str):
    # Read the JSON file
    with open(file_path, "r") as file:
        data = json.load(file)
    
    # Add the new value
    data["new_key"] = new_value  
    
    # Write the modified JSON data back to the file
    with open(file_path, "w") as file:
        json.dump(data, file)
    
    return {"message": "Value added successfully"}


with open(file_path, "r") as file:
    restaurants_data = json.load(file)["restaurants"]
    
@app.get("/search")
def search_dish(dish: str = Query(default='', title="Dish Name")):

    restaurants_with_dish = []
    for restaurant in restaurants_data:
        for menu in restaurant["menu"]:
            if dish.lower() in menu:
                restaurants_with_dish.append(restaurant["name"])
                break
    return {"restaurants": restaurants_with_dish}    

# write an api which takes restaurant name as input and displays all the dishes in the restaurant
@app.get("/get_menu")
def search_dish(restaurant_name:str):
      for restaurant in restaurants_data:
           if restaurant["name"].lower() == restaurant_name.lower():
                return restaurant["menu"]
      return ""   
          
    

    
    