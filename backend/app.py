from flask import Flask, request, jsonify
# from flask_cors import CORS
import joblib
import os

# Initialize the Flask app
app = Flask(__name__)
# CORS(app)  # Allow frontend to communicate with backend

# Load the model (adjust the path if needed)
model_path = os.path.join('spam_model.pkl')
model = joblib.load(model_path)

# Prediction function
def predict_email(email_text):
    prediction = model.predict([email_text])

    if prediction[0] == 1:
        return "Spam"
    else:
        return "Not Spam"

# API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    email_text = data.get('email')

    if not email_text:
        return jsonify({'error': 'No email text provided'}), 400

    result = predict_email(email_text)

    return jsonify({'result': result})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
