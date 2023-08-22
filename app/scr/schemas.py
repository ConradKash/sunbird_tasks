from pydantic import BaseModel

class _predictBase(BaseModel):
    text: str
    language: str
    process_time: str
    
    class Config:
        orm_mode = True