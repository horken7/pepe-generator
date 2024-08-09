import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
