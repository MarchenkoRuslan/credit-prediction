from flask import Flask, request, jsonify
import pandas as pd
from pycaret.classification import load_model, predict_model
import logging

# curl -X POST -H "Content-Type: application/json" -d @input.json http://127.0.0.1:8000/predict

app = Flask(__name__)

# Setting up logging
logging.basicConfig(level=logging.DEBUG,
                    filename='../flask_log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loading model
model = load_model('best_model_pycaret')

@app.route('/')
def get_root():
    app.logger.info("Root endpoint called")
    return {"message": "Welcome to the prediction API"}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        app.logger.info("Prediction request received")

        # Getting data in JSON format
        data = request.get_json(force=True)
        app.logger.debug(f"Input data: {data}")

        # Converting data to DataFrame
        features = pd.DataFrame(data['features'])
        app.logger.debug(f"DataFrame: {features}")

        # Getting a prediction
        predictions = predict_model(model, data=features)
        app.logger.debug(f"Predictions DataFrame: {predictions}")

        # Returning the result
        result = predictions[['prediction_label', 'prediction_score']].to_dict(orient='records')
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
