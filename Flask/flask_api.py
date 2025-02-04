from flask import Flask, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

data = []  # Temporary storage for received data

@app.route('/submit', methods=['POST'])
def submit():
    try:
        req_data = request.json
        data.append(req_data)

        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_data', methods=['GET'])
def get_data():
    df = pd.DataFrame(data)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.10', port=8501)