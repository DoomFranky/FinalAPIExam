from fastapi import FastAPI
from type import List
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

class phones(BaseModel):
    id: str
    brand: str
    models: str
    class characteristique:
        ram_memory: int
        rom_memory: int

phone= List(Phones)

app = FastAPI()


@app.get("/health")
def ping():
    return Response(content='OK',status_code=200,media_type='text/plain')

@app.post("/phones")
def postPhones(thePhone = List(Phones)):
    thePhone.extend()
    return thePhone

def serializing():
    serialized = []
    for p in phone:
        serialized.append(p.model_dump())
    return serialized
@app.get("/phones")
def getPhones():
    return JSONResponse(content=serializing(),status_code='200',media_type='application/json')

@app.get("/phones")
def getPhonesById(id: Request):
    thePhone: serializing().id
    return JSONResponse(content=thePhone,status_code='200',media_type='application/json')
@app.put("/phones")
def getPhonesById(id :Request):
    return null