import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

heart_model = pickle.load(open('C:/Users/Rinku/Desktop/heart_disease_dataset/heart_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Prediction System',
                          
                          ['Heart Disease Prediction'],
                          icons=['heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Prediction using ML')
    
    
    # getting the input data from the user age anaemia creatinine_phosphokinase diabetes ejection_fraction high_blood_pressure platelets serum_creatinine serum_sodium sex smoking time
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('enter your age 1 to 100')
        
    with col2:
        anaemia = st.text_input('if you are suffering from anamemia enter 1 for yes and 0 for no')
    
    with col3:
        creatinine_phosphokinase = st.text_input('enter level of creatinine_phosphokinase')
    
    with col1:
        diabetes = st.text_input('if patient is suffering from diabetes 1 for yes 0 for no')
    
    with col2:
        ejection_fraction = st.text_input('enter level of ejection_fraction')
    
    with col3:
        hbp = st.text_input('if patient is suffering from high blood pressure 1 for yes 0 for no')
    
    with col1:
        platelets = st.text_input('enter platelets count')
    
    with col2:
        serum_creatinine = st.text_input('enter level of serum createnine ')
    
    with col3:
        serum_sodium = st.text_input('enter level of serum sodium')
    
    with col1:
        sex = st.text_input("enter sex 1 for male 0 for female")
    
    with col2:
        smoking = st.text_input("if patient use to smoke 0 for no 1 for yes ")
    
    with col3:
        time = st.text_input("enter follow-up period in days from 0 to 365")
    
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('heart Test Result'):
        heart_prediction = heart_model.predict([[age, anaemia ,creatinine_phosphokinase, diabetes, ejection_fraction, hbp, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is suffering from heart diseases'
        else:
          heart_diagnosis = 'The person is not suffering from heart diseases'

    st.success(heart_diagnosis)