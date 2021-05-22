# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:29:49 2020

@author: abhis
"""
    
#1. Import Libraries
#request - Request to send GET and POST
    
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
    
#2. Create the Flask App Object
    
app = Flask(__name__)
    
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

#3. Index Route 

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict')
def predict_note_authentication():
    varience = request.args.get('varience')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy  = request.args.get('entropy')
    
    prediction = classifier.predict([[varience,skewness,curtosis,entropy]])
    
    if(prediction[0]>0.5):
        prediction = 'Fake Note'
    else:
        prediction = 'It is a Bank Note'
        
    return{
            'prediction':prediction
            }
    
@app.route('/predict_file',methods = ['POST'])
def predict_note_file():
    
    df_test = pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(df_test)
    
    if(prediction[0]>0.5):
        prediction = 'Fake Note'
    else:
        prediction = 'It is a Bank Note'
        
    return{
            'prediction':list(prediction)
            }
    
    
if __name__ == '__main__':
    app.run(debug=False)

