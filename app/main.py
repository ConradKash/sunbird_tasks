from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from pathlib import Path
from nltk.tokenize import word_tokenize
app = FastAPI()

__version__ = "0.1.0"

classes = [
    'Acholi',
    'English',
    'lugbara',
    'luganda',
    'Runyankole',
    'Ateso'
]
def dataPro(thWord):
  rm = thWord
  thWord = thWord.lower()
  thWord = thWord.split()
  thWord = word_tokenize(str(thWord))
  thWord = ' '.join(thWord)
  return thWord
def predictm(ptext):
    dataPro(ptext)
    x = cv.transform([ptext]).toarray()
    lang = model.predict(x)
    return classes[lang[0]]

model = pickle.load(open("/model.pkl", "rb"))
cv = pickle.load(open("/transform.pkl", "rb"))


class TextIn(BaseModel):
    text: str
    
class PredictionOut(BaseModel):
    language: str
    
app.get("/")
def home():
    return {"Model Version: ": __version__ }

app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predictm(payload.text)
    return {"Language": language}