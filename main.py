from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/nice")
def read_root():
    return "666，我超級帥，脊椎"

@app.post("/items/")
def create_item(item: Item):
    print(f"Received item: {item}")
    return{"message": "Item received", "item": item}