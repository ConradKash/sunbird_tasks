from fastapi import FastAPI, Request, request, render_template
import uvicorn
import sklearn
import pickle
import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
import io
import requests

#importing the dataset
url="https://raw.githubusercontent.com/SunbirdAI/salt/main/v1.2/salt-test-v1.2.jsonl"
s=requests.get(url).content
data =pd.read_json(io.StringIO(s.decode('utf-8')))

app = FastAPI(__name__)
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predict', methods= ["POST"])

def predict():
    y = data["language"]
    
    #label Encoding
    y = le.fit_transform(y)
    
    #Loading the model and cv for deploment
    model = pickle.load(open("model.pki", "rb"))
    cv = pickle.load(open("transform.pki", "rb"))
    
    if request.method == "POST":
        #prompting a user to input something
        text = request.form["text"]
        
        #Processing the text
        text = re.sub(r'[[]]', '', text)
        text = text.lower()
        dat = [text]
        
        #creating a vector
        vect = cv.transform(dat).toarray()
        
        #prediction
        my_pred = model.predict(vect)
        my_pred = le.inverse_transform(my_pred)
    
    return render_template("home.html", pred="The above text is in {}".format(my_pred[0]))
        
if __name__ == "__main__":
    app.run(debug=True)