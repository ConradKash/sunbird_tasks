from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.model import predicted_language
from time import perf_counter

app = FastAPI()

    
class Prediction(BaseModel):
    text: str
    language: str
    proocess_time: float
    
    
@app.get("/")   
def root():
    return {"Model Version LanguageID app"}

@app.post("/predict", response_model = Prediction)
def predict(payload: Prediction):
    start_time = perf_counter()
    
    predict_language = predicted_language(payload.text)
    
    end_time = perf_counter()
    
    procrss_time = end_time - start_time
    return Prediction(text = payload.text, language = predict_language, proocess_time = procrss_time)


