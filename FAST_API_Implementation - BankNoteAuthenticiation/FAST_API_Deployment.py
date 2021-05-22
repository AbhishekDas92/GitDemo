# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:55:41 2020

@author: abhis
"""

# 1. Import Library

import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
from Wine_Data import WinePrediction
import pickle
import pandas as pd
import numpy as np


# 2. Create the app object

app = FastAPI()
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)


app1 = FastAPI()
pickle_wine_in = open('Wine_Prediction.pkl','rb')
clf_tree_classifier = pickle.load(pickle_wine_in)

# 3. Index route, opens automatically on https://127.0.0.1:8000

@app.get('/')
def index():
    return {'message':'Hello , stranger'}

# 4. Route with a single parameter , returns the parameter within a message 
     # Located at :https://127.0.0.1:8000/AnyNameHere
     
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to Abhishek Das Practice Channel':f'{name}'}

#5. Expose the Linear Regression Expose Functionality

@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    print(data)
    print('Hello')
    varience = data['varience']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy =  data['entropy']
    
    #print(classifier.predict([[varience,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[varience,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction = 'Fake Note'
    else:
        prediction = 'It is a Bank Note'
        
    return{
            'prediction':prediction
            }
    
@app1.post('/predict')
def predict_wine_quality(data:WinePrediction):
    data = data.dict()
    print(data)
    fixed_acidity = data['fixed_acidity']
    volatile_acidity = data['volatile_acidity']
    citric_acid = data['citric_acid']
    residual_sugar = data['residual_sugar']
    chlorides =  data['chlorides']
    free_sulfur_dioxide = data['free_sulfur_dioxide'] 
    total_sulfur_dioxide = data['total_sulfur_dioxide']
    density =  data['density']
    pH = data['pH']
    sulphates = data['sulphates']
    
    alcohol = data['alcohol'] 
    
    prediction = clf_tree_classifier.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]])
    if(prediction[0]>0.5):
        prediction = 'Bad Wine Quality'
    else:
        prediction = 'It is a Good Wine Quality Note'
        
    return{
            'prediction':prediction
            }      
        
# 6. Run the Unicorn App
    
    if __name__ == 'main':
        uvicorn.run(app1,host='127.0.0.1',port=8000)
        

### uvicorn FAST_API_Deployment:app --reload    