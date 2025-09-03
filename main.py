from fastapi import FastAPI

class Phones:
    id: String
    brand: String
    models: String
    class characteristique:
        ram_memory: int
        rom_memory: int


app = FastAPI()


@app.get("/health")
def ping():
    return Response(content='OK',status_code=200,media_type='text/plain')

@app.post("/phones")
def postPhones():
    return null

@app.get("/phones")
def getPhones():
    return null

@app.get("/phones")
def getPhonesById(id: Request):
    return null
@app.put("/phones")
def getPhonesById(id :Request):
    return null