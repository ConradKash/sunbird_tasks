from pydantic import BaseModel

class PredictBase(BaseModel):
    text: str

class predictout(PredictBase):
    language: str
    process_time: float  
        
    class Config:
        orm_mode = True