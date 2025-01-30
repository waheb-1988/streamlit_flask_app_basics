import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 40, 28],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
}
df = pd.DataFrame(data)

# Streamlit App Title
st.set_page_config(layout="wide")
st.title("Advanced Streamlit Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Filter Data", "Statistics", "About"])

if page == "Home":
    st.header("Welcome to the Dashboard")
    st.write("Use the sidebar to navigate between different sections.")

elif page == "Filter Data":
    st.header("Filter Data")
    search_query = st.text_input("Search by Name:")
    if search_query:
        filtered_df = df[df["Name"].str.contains(search_query, case=False, na=False)]
    else:
        filtered_df = df
    st.write("### Filtered Results:")
    st.dataframe(filtered_df)

elif page == "Statistics":
    st.header("Statistics Overview")
    st.write("### Summary Statistics")
    st.write(df.describe())

elif page == "About":
    st.header("About This App")
    st.write("This is a simple Streamlit dashboard with multiple sections.")