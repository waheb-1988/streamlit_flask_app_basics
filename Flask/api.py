from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Helen", "Ian", "Jack"],
    "Age": [25, 30, 35, 40, 28, 33, 27, 45, 31, 29],
    "Salary": [50000, 60000, 55000, 70000, 48000, 62000, 51000, 73000, 59000, 56000],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "San Francisco", "Dallas", "Seattle", "Boston", "Denver"],
    "Experience": [2, 5, 7, 10, 3, 6, 4, 12, 5, 4]
}
df = pd.DataFrame(data)

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(df.to_dict(orient="records"))

@app.route('/filter_data', methods=['GET'])
def filter_data():
    name = request.args.get('name', default="", type=str)
    filtered_df = df[df["Name"].str.contains(name, case=False, na=False)]
    return jsonify(filtered_df.to_dict(orient="records"))

@app.route('/get_statistics', methods=['GET'])
def get_statistics():
    stats = df.describe().to_dict()
    return jsonify(stats)

@app.route('/add_data', methods=['POST'])
def add_data():
    """Adds new data to the dataset"""
    global df
    new_entry = request.json  # Get JSON data from Postman
    print("Received Data:", new_entry)  # Debugging
    
    if not all(key in new_entry for key in ["Name", "Age", "Salary", "City", "Experience"]):
        return jsonify({"error": "Missing fields"}), 400
    
    new_df = pd.DataFrame([new_entry])  # Convert new data to DataFrame
    df = pd.concat([df, new_df], ignore_index=True)  # Append new data
    return jsonify({"message": "Data added successfully!", "new_data": df.to_dict(orient="records")})

if __name__ == '__main__':
    app.run(debug=True)




## http://127.0.0.1:5000/get_data
## http://127.0.0.1:5000/filter_data?name=Alice