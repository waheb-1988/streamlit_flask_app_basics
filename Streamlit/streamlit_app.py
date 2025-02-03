import streamlit as st
import pandas as pd
import subprocess

# Title for Streamlit app
st.title("Excel File Processor")
st.write("This is a simple app to interact with the Excel file.")

# Sidebar for file upload
st.sidebar.title("Upload Excel File")
uploaded_file = st.sidebar.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

# Show file preview and data in different pages
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    page = st.sidebar.radio("Choose a page", ["Home", "Preview", "Summary", "Column Names", "Shape"])

    if page == "Preview":
        st.write("Preview of the file:")
        st.dataframe(df.head(5))  # Show first 5 rows

    elif page == "Summary":
        st.write("Summary Statistics:")
        st.write(df.describe())  # Show summary stats

    elif page == "Column Names":
        st.write("Columns in the file:")
        st.write(df.columns)  # Show column names

    elif page == "Shape":
        st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")  # Show dataset shape
else:
    st.write("Upload an Excel file to start.")

# You can use subprocess to run Flask in a separate process
def run_flask():
    subprocess.run(["python", "flask_app.py"])

if __name__ == "__main__":
    run_flask()
