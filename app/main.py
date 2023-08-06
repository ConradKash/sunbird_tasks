from fastapi import FastAPI
from pydantic import BaseModel
from app.model import _version__, predictm

app = FastAPI()

class TextIn(BaseModel):
    text: str
    
class PredictionOut(BaseModel):
    language: str
    
app.get("/")
def home():
    return {"Model Version: ": _version__ }

app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predictm(payload.text)
    return {"Language": language}