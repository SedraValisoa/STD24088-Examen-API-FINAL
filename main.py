from fastapi import FastAPI,Response,HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Examen API Final", description="",version="1.0.0")


"""
Model:
"""

class Charateristic(BaseModel):
    ram_memory: int
    rom_memory: int
# end class
class Phone(BaseModel):
    id: int
    brand: str
    model: str
    characteristics: Charateristic
# end class
""""
DAO:
"""
phone_db: List[Phone] = []
charteristic: List[Charateristic] = []






@app.get("/ping")
def read_root():
    return {"message":"pong"}

@app.get("/health")
def read_health():
    return Response(content="OK",media_type="text/plain")
    
# end def

@app.post("/phone")
def create_phone(phone: List[Phone]):
    for p in phone:
        phone_db.append(p)
    return Response(content=phone_db,media_type="application/json",status_code=201)
# end def
def add_phone(phone: List[Phone]):
    for p in phone:
        phone_db.append(p)
    return phone_db
@app.get("/phones")
def get_phone(id: int):
    """
    Purpose: one
    """
    return phone_db
    
# end def
@app.get("/phones/{id}")
def get_phone_by_id(id):
    result: Phone = phone_db[id]
    if (result == None):
        raise HTTPException(status_code=404,detail="Phone not found")
    # end if
    return Response(content=result.json(),media_type="application/json")
@app.put("/phones/{phone_id}/characteristics")
def update_phone(phone_id: int,characteristics: Charateristic):
    result: Phone = phone_db[id]
    if (result == None):
        raise HTTPException(status_code=404,detail="Phone not found")
    # end if
    result.characteristics = characteristics
    return Response(content=result.json(),media_type="application/json")