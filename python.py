from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"}), 200

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Mock prediction logic (replace with your actual model)
    input_value = data.get("input")
    if input_value is None:
        return jsonify({"error": "Missing 'input' field"}), 400

    # For demonstration, we just return input length as "prediction"
    prediction = len(str(input_value))  

    return jsonify({
        "input": input_value,
        "prediction": prediction
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

