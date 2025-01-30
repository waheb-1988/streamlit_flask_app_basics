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
st.title("Simple Streamlit Dashboard")

# Text Input for Filtering
search_query = st.text_input("Search by Name:")

# Filter DataFrame based on input
if search_query:
    filtered_df = df[df["Name"].str.contains(search_query, case=False, na=False)]
else:
    filtered_df = df

# Display Filtered Results
st.write("### Filtered Results:")
st.dataframe(filtered_df)
