from pydantic import BaseModel

class language_model(BaseModel):
    language: str
    text: list