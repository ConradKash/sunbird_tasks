from pydantic import BaseModel

class PredictBase(BaseModel):
    text: str
    language: str
    process_time: float
    
    class Config:
        orm_mode = True