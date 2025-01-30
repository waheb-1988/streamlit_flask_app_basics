**README.md**
```
# Streamlit Dashboard with Flask API

## Overview
This project consists of a Streamlit dashboard that fetches and displays data from a Flask API. Users can send data using Postman and view the updated results in the dashboard.

## Features
- Streamlit dashboard with a sidebar and multiple pages
- Flask API to receive and retrieve data
- Postman integration for data submission
- Dynamic data visualization

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/streamlit-flask-dashboard.git
   cd streamlit-flask-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
### Start the Flask API
```bash
python flask_app.py
```

### Start the Streamlit App
```bash
streamlit run streamlit_dashboard.py
```

## API Usage (Postman)
### Add Data (POST Request)
- URL: `http://127.0.0.1:5000/add_data`
- Body (JSON format):
  ```json
  {
      "Name": "John Doe",
      "Age": 32,
      "City": "San Francisco"
  }
  ```

### Get Data (GET Request)
- URL: `http://127.0.0.1:5000/get_data`

## License
MIT License
