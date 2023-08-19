from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predicted_language
from typing import Any

app = FastAPI()


class TextIn(BaseModel):
    text: str
    
    
class PredictionOut(BaseModel):
    language: str
    
class UserPost(BaseModel):
    name: str
    body: str
    
@app.get("/")   
def root():
    return {"Model Version LanguageID app"}

@app.post("/predict", response_model = PredictionOut)
def predict(payload: TextIn):
    predict_language = predicted_language(payload.text)
    print()
    return PredictionOut(language = predict_language)

