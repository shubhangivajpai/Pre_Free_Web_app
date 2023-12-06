# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:11:31 2022

@author: shubhangi vajpai
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model=pickle.load(open('C:/Users/shubhangi vajpai/OneDrive/Desktop/predicting health risks/trained_model1.sav','rb'))


# creating a function for Prediction

def health_risks_prediction(inpArray):
    #print("---------------------------------")
    #print("       DecisionTreeClassifier")
   # print("Level of Risk:1-3   low->1,high->3")
    #print("__________________________________")
    inpFrame=['Enter Age of Patient:','Enter systolic Blood Pressure of Patient:','Enter Diastolic Blood Pressuree of Patient:','Enter Blood Glucose Level of Patient:','Enter Body Temperarature of  Patient:','Enter Heart Rateof Patient:',]
    inpArray=list()
    for i in  range(6):
      temp=input(inpFrame[i])
      inpArray.append(float(temp))

    patientPredict=loaded_model.predict([inpArray])
    #print("________________________________________")
    return ("Risk Level of patient is:",patientPredict[0])
    #print('-----------------------------------------')

def main():
    
    
    #giving a title
    st.title('Predicting Health Risks for Pregnant Patients Web App')
    
    
    # getting the input data from the user
    
    Age=st.text_input('Age of the Patient')
    SystolicBP=st.text_input('Systolic BP of Patient')
    DiastolicBP=st.text_input('Diastolic BP of the Patient')
    BS=st.text_input('Blood glucose Levels of the Patient')
    BodyTemp=st.text_input('Body Temp of the Patient')
    HeartRate=st.text_input('Heart Rate of the Patient')
    
    # code for Prediction
    
    diagnosis=''
    
    # creating a button for Prediction
    if st.button('Health Risks test Result'):
        diagnosis=health_risks_prediction([Age,SystolicBP,DiastolicBP,BS, BodyTemp,HeartRate])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
        
    
    
    