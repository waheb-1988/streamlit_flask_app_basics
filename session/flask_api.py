from flask import Flask,request,jsonify
import pandas as pd

app = Flask(__name__)
data = []
@app.route('/submit',methods=['POST'])
def submit():
    req = request.json
    data.append(req)
    print(data)
    return data

@app.route('/get_data',methods=['GET'])

def get_data():
    
    df= pd.DataFrame(data)
    
    return df.to_json(orient='records')


if __name__== '__main__':
    
    app.run(debug= True, host='192.168.100.10', port= '8501')
