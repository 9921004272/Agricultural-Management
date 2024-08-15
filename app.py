from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib
import os

app = Flask(__name__)

# Load the machine learning model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    # Replace with actual authentication logic
    if username == 'admin' and password == 'password':
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']
    mobile_number = data['mobileNumber']
    email = data['email']
    # Replace with actual signup logic
    return jsonify({'success': True})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    moisture = data['moisture']
    temperature = data['temperature']
    ph = data['ph']
    fertilizer = data['fertilizer']
    # Predict using the machine learning model
    prediction = model.predict([[moisture, temperature, ph, fertilizer]])
    return jsonify({'success': True, 'data': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
