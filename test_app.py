import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def test_artifacts_exist():
    model_path = os.path.join(BASE_DIR, 'car_price_model.pkl')
    preprocessor_path = os.path.join(BASE_DIR, 'car_preprocessor.pkl')
    
    assert os.path.exists(model_path), f"Model artifact missing at {model_path}"
    assert os.path.exists(preprocessor_path), f"Preprocessor artifact missing at {preprocessor_path}"