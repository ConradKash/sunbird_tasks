import fastapi as _fastapi
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.model import predicted_language
from time import perf_counter
import sqlalchemy.orm as _orm
from app.scr import services as _services, schemas as _schemas

_services.create_database()

app = _fastapi.FastAPI()   
    
    
@app.get("/")   
def root():
    return {"Model Version LanguageID app"}

@app.post("/predict", response_model = _schemas.predictout)
def predict(payload: _schemas.PredictBase, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    start_time = perf_counter()
    
    language = predicted_language(payload.text)
    
    end_time = perf_counter()
    
    process_time = end_time - start_time

    return _services.send_report(db=db, prediction=_schemas.predictout(text=payload.text, language = language, process_time = process_time))