from flask import Flask, request, jsonify
import requests
import joblib
import numpy as np

model = joblib.load("random_fores.pkl")


app = Flask(__name__)

@app.route('/predict', methods= ['POST'])

def predict():
    
    data= request.json
    
    features = np.array(data['features']).reshape(1,-1)

    prediction = model.predict(features)
    prediction_proba = model.predict_proba(features)
    
    return jsonify({
        
        "prediction" : int(prediction[0]),
        "prediction_proba" : prediction_proba.tolist()[0]
        
        
    })

if __name__ == '__main__':
    
    app.run(debug=True,host='192.168.100.10', port= '8501')
    
