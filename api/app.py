from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load(open('../output/iris_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(port=5000)
    
# Example JSON input
# {
#     "features": [
#         5.1,
#         3.5,
#         1.4,
#         0.2
#     ]
# }