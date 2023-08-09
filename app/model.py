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
def text_processing(translate_text):
  translate_text = translate_text .lower()
  translate_text  = translate_text .split()
  translate_text  = word_tokenize(str(translate_text ))
  translate_text  = ' '.join(translate_text )
  return translate_text 
def predicted_language(ptext):
    l =text_processing(ptext)
    x = cv.transform([l]).toarray()
    lang = model.predict(x)
    return classes[lang[0]]