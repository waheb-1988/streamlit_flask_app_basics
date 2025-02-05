import streamlit as st 
import requests
import pandas as pd
def main():
    st.title("Diabetes Prediction Input Form")
    Pregnancies= st.number_input("Pregnancies", min_value=0, step=1)
    Glucose= st.number_input("Glucose", min_value=0, step=1)
    BloodPressure = st.number_input("BloodPressure", min_value=0, step=1)
    SkinThickness = st.number_input("SkinThickness", min_value=0, step=1)
    Insulin = st.number_input("Insulin", min_value=0, step=1)
    BMI = st.number_input("BMI", min_value=0,  step=1)
    DiabetesPedigreeFunction= st.number_input("DiabetesPedigreeFunction", min_value=0,  step=1)
    Age= st.number_input("Age", min_value=0,  step=1)
    
    if st.button("Submit") :
        data = {
            
            'Pregnancies' : Pregnancies,
            'Glucose' : Glucose,
            'BloodPressure' :BloodPressure,
            'SkinThickness' : SkinThickness,
            'Insulin' : Insulin,
            'BMI': BMI,
            'DiabetesPedigreeFunction' : DiabetesPedigreeFunction,
            'Age' :  Age,
        }
        response = requests.post("http://192.168.100.10:8501/submit", json=data)
    if st.button('View_data'):
        response = requests.get("http://192.168.100.10:8501/get_data")
        df = pd.DataFrame(response.json())
        st.write(df)    
if __name__== "__main__":
    
    main()