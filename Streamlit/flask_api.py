import streamlit as st
import pandas as pd
import threading
from flask import Flask, request, jsonify
import io

app = Flask(__name__)

# Flask route
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    df = pd.read_excel(file)
    return jsonify({
        "columns": df.columns.tolist(),
        "shape": df.shape,
        "head": df.head(5).to_dict(orient='records')
    })

def run_flask():
    app.run(debug=True, use_reloader=False)

# Start Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

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
