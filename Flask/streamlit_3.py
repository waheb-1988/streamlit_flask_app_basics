import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# API Base URL
API_URL = "http://127.0.0.1:5000"

st.set_page_config(layout="wide")
st.title("Streamlit Dashboard with Flask API")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "View Data", "Statistics", "Graphics", "About"])

if page == "Home":
    st.header("Welcome to the Dashboard")
    st.write("Use the sidebar to navigate between different sections.")

elif page == "View Data":
    st.header("View Data")
    response = requests.get(f"{API_URL}/get_data")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.error("Failed to fetch data from API")

elif page == "Statistics":
    st.header("Statistics Overview")
    response = requests.get(f"{API_URL}/get_statistics")
    if response.status_code == 200:
        stats = response.json()
        st.write(pd.DataFrame(stats))
    else:
        st.error("Failed to fetch statistics")

elif page == "Graphics":
    st.header("Data Visualization")
    response = requests.get(f"{API_URL}/get_data")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        # Create a histogram of ages
        st.subheader("Age Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df["Age"], bins=10, kde=True, ax=ax)
        st.pyplot(fig)

        # Salary vs Experience scatter plot
        st.subheader("Salary vs Experience")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df["Experience"], y=df["Salary"], ax=ax)
        st.pyplot(fig)
    else:
        st.error("Failed to fetch data from API")

elif page == "About":
    st.header("About This App")
    st.write("This is a Streamlit dashboard connected to a Flask API.")
