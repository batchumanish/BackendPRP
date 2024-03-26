from pydantic import BaseModel
from beanie import Document

class User(BaseModel):
    name:str
    email:str
    password:str

class Gg(Document): 
    name:str
    age:int   
    