from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/nice")
def read_root():
    return "666，我超級帥，脊椎"