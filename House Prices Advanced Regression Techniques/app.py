# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:26:47 2020

@author: abhis
"""

#1. Import Package
import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle


#2. Create Flask Object

app = Flask(__name__)
model = pickle.load(open('House_Price.pkl','rb'))

#3. Create Method

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    int_feature = [int(x) for x in request.form.values]
    final_features = [np.array(int_feature)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0],2)
    
    return render_template('index.html',prediction_text='House price should be {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
