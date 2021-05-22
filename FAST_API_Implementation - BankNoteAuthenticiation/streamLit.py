# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:33:55 2020

@author: abhis
"""
import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
from flask import Flask, request



#1. Load ML Model
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction
    
    return "Hello The answer is"+str(prediction)


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
