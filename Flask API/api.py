import joblib  
from flask import Flask ,  request, jsonify 
import functinos 

app = Flask(__name__)  

@app.route("/predict" , methods=['POST'])
def predict() : 
    data = request.json 
    x = data.get("features", [])
    x[1] = functinos.encode_geography(x[1])
    x[2] = functinos.encode_gender(x[2])
    x_scaled = functinos.scaling(x) 
    prediction = int(functinos.model_predict(x_scaled))
    return jsonify({'prediction' : prediction}) 

if __name__ == "__main__" : 
    app.run(debug=True)