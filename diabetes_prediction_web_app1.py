# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:25:34 2023

@author: rajka
"""

import numpy as np
import pickle
import streamlit as st


#loading saved model
loaded_model = pickle.load(open('C:/aaaaaa/CODING/ML/basics/Model dep/z spider practice/1/trained_model.sav','rb'))

#predicting function
def diabetes_prediction(input_data):
    np_input = np.asarray(input_data)
    npre = np_input.reshape(1,-1)
    predict = loaded_model.predict(npre)
    print(predict)
    if predict[0]==0:
        return "person is not diabetic"
    else :
        return "person is diabetic"



def main():
    
    #giving title
    st.title('Diabetic prediction Web App')
    
    #getting input data from user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Age of the person')
    
    
    #code for prediction
    
    diagnosis = ''
    
    #creating button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()
    


        
        
    
    
    