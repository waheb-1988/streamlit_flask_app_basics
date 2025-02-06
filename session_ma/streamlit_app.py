import streamlit as st 
import requests

# Streamlit app title
st.title("Logistic Regression Prediction App")

# Input fields for features
st.header("Enter the Features for Prediction")
feature_1 = st.number_input("Feature 1 (e.g., Pregnancies)", value=0, step=1)
feature_2 = st.number_input("Feature 2 (e.g., Glucose)", value=0.0)
feature_3 = st.number_input("Feature 3 (e.g., Blood Pressure)", value=0.0)
feature_4 = st.number_input("Feature 4 (e.g., Skin Thickness)", value=0.0)
feature_5 = st.number_input("Feature 5 (e.g., Insulin)", value=0.0)
feature_6 = st.number_input("Feature 6 (e.g., BMI)", value=0.0)
feature_7 = st.number_input("Feature 7 (e.g., Diabetes Pedigree Function)", value=0.0)
feature_8 = st.number_input("Feature 8 (e.g., Age)", value=0, step=1)

features = [feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,feature_7,feature_8]

if st.button('Get Prediction'):
    
    payload = {"features":features}
  
    API_Url= "http://192.168.100.10:8501/predict"
    response = requests.post(API_Url, json=payload)
    
    if response.status_code == 200:
        
        result = response.json()
        
        st.success(f"Prediction : {result['prediction']}")
        st.success(f"Prediction : {result['prediction_proba']}")
 