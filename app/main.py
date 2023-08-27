import fastapi as _fastapi
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.model import predicted_language
from time import perf_counter
import sqlalchemy.orm as _orm
from app.scr import services as _services, schemas as _schemas

_services.create_database()

app = _fastapi.FastAPI()


class TextIn(BaseModel):
    text: str
    
    
class PredictionOut(BaseModel):
    language: str
    process_time: float
    
    
@app.get("/")   
def root():
    return {"Model Version LanguageID app"}

@app.post("/predict", response_model = _schemas.PredictBase)
def predict(payload: _schemas.PredictBase, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    start_time = perf_counter()
    
    payload.language = predicted_language(payload.text)
    
    end_time = perf_counter()
    
    payload.process_time = end_time - start_time

    return _services.send_report(db=db, prediction=_schemas.PredictBase)
