from fastapi import FastAPI,HTTPException
from starlette.responses import Response, JSONResponse
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
    
    phone_db.extend(phone)
    phone_serialized = serialize_phone()
    return JSONResponse(content=phone_serialized, status_code=201, media_type="application/json")
# end def


def serialize_phone():
    phone_serialized = []
    for phone in phone_db:
        phone_serialized.append(phone.model_dump())
    return phone_serialized




@app.get("/phones")
def list_posts():
    return JSONResponse(content=serialize_phone(), status_code=200, media_type="application/json")
    
# end def
@app.get("/phones/{id}")
def get_phone_by_id(id):
    result: Phone = phone_db[id]
    if (result == None):
        raise HTTPException(status_code=404,detail="Phone not found")
    # end if
    return JSONResponse(content=result,media_type="application/json")

