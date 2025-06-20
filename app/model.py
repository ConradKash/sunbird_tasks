import pickle
from pathlib import Path
import nltk
import joblib
nltk.download('punkt')
from nltk.tokenize import word_tokenize


BASE_DIR = Path(__file__).resolve(strict=True).parent

   
with open(f"{BASE_DIR}/model.pkl", "rb") as f:
    model = pickle.load(f)
   
     
with open(f"{BASE_DIR}/transform.pkl", "rb") as f:
    cv = pickle.load(f)
    
classes = [
    'Acholi',
    'English',
    'Lugbara',
    'Luganda',
    'Runyankole',
    'Ateso'
]
pipeline = True
   
if pipeline == True:
    def text_processing(translate_text):
        translate_text = translate_text.lower()
        translate_text = translate_text.split()
        translate_text = word_tokenize(str(translate_text))
        translate_text = ' '.join(translate_text)
        return translate_text     

    def predicted_language(ptext):
        process_text = text_processing(ptext)
        x = cv.transform([process_text]).toarray()
        lang = model.predict(x)
        return classes[lang[0]]
else:
    def predicted_language(ptext):
        samples = [ptext]
        prediction = model.predict(samples)
        if prediction == ['ach']:
            lang = 0
        elif prediction == ['eng']:
            lang = 1
        elif prediction == ['lgg']:
            lang = 2
        elif prediction == ['lug']:
            lang = 3
        elif prediction == ['nyn']:
            lang = 4
        elif prediction == ['teo']:
            lang = 5           
            
        return classes[lang]
    
predicted_language('')