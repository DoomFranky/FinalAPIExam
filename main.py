from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return JSONResponse({"message": f"Hello"}, status_code=200);
