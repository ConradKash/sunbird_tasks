from fastapi import FastAPI
from pydantic import BaseModel
from model import _version__ as model_Version, predicted_language


app = FastAPI()

class TextIn(BaseModel):
    text: str
    
class PredictionOut(BaseModel):
    language: str
    
@app.get("/")
def root():
    return {"Model Version": model_Version}

@app.get("/{text}")
def trans_api(text):
    return {"The language is in": predicted_language(text)}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predicted_language(payload.text)
    return PredictionOut(language = language)
