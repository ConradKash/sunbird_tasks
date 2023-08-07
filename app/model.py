import pickle
from pathlib import Path
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

_version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


    
with open(f"{BASE_DIR}/model-{_version__}.pkl", "rb") as f:
    model = pickle.load(f)
    
with open(f"{BASE_DIR}/transform-{_version__}.pkl", "rb") as f:
    cv = pickle.load(f)
    
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

print(predictm('Nkwagala nyooo'))