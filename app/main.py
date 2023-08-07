from fastapi import FastAPI
from pydantic import BaseModel
from model import _version__ as model_Version, predictm


app = FastAPI()

class TextIn(BaseModel):
    text: str
    
class PredictionOut(BaseModel):
    language: str
    
@app.get("/")
def root():
    return {"Model Version": model_Version}

@app.get("/{entText}")
def transApi(entText):
    return {"The language is in": predictm(entText)}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predictm(payload.text)
    return {"Language": language}
