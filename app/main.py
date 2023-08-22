from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.model import predicted_language
from time import perf_counter
from app.scr import services as _services

_services.create_database()

app = FastAPI()


class TextIn(BaseModel):
    text: str
    
    
class PredictionOut(BaseModel):
    language: str
    process_time: float
    
    
@app.get("/")   
def root():
    return {"Model Version LanguageID app"}

@app.post("/predict", response_model = PredictionOut)
def predict(payload: TextIn):
    start_time = perf_counter()
    
    predict_language = predicted_language(payload.text)
    
    end_time = perf_counter()
    
    process_time = end_time - start_time

    return PredictionOut(language = predict_language, process_time = process_time)
