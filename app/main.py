from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predicted_language
from typing import Any

app = FastAPI()


class TextIn(BaseModel):
    text: str
    
    
class PredictionOut(BaseModel):
    language: str
    
    
@app.get("/")   
def root():
    return {"Model Version LanguageID app"}

@app.post("/predict", response_model = PredictionOut)
def predict(payload: TextIn):
    predict_language = predicted_language(payload.text)
    return PredictionOut(language = predict_language)

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]