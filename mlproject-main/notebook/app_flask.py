import os
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import datetime

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'car_price_model.pkl')
PREPROCESSOR_PATH = os.path.join(BASE_DIR, 'car_preprocessor.pkl')

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        
        # Calculate Car_Age if Year is provided instead
        if 'Year' in df.columns and 'Car_Age' not in df.columns:
            current_year = datetime.datetime.now().year
            df['Car_Age'] = current_year - df['Year']
            df = df.drop(columns=['Year'])
            
        processed_data = preprocessor.transform(df)
        prediction = model.predict(processed_data)[0]
        return jsonify({"predicted_price": round(float(prediction), 2)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)