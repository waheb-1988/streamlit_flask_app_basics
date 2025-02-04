import streamlit as st
import requests
import pandas as pd

def main():
    st.title("Diabetes Prediction Input Form")
    
    # Input fields
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("Age", min_value=0, step=1)
    
    # Submit button
    if st.button("Submit"):
        data = {
            "Pregnancies": pregnancies,
            "Glucose": glucose,
            "BloodPressure": blood_pressure,
            "SkinThickness": skin_thickness,
            "Insulin": insulin,
            "BMI": bmi,
            "DiabetesPedigreeFunction": dpf,
            "Age": age
        }
        response = requests.post("http://192.168.100.10:8501/submit", json=data)
        if response.status_code == 200:
            st.success("Data submitted successfully!")
        else:
            st.error("Error submitting data")
    
    # View stored data
    if st.button("View Data"):
        response = requests.get("http://192.168.100.10:8501/get_data")
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            st.write(df)
        else:
            st.error("Error fetching data")

if __name__ == "__main__":
    main()