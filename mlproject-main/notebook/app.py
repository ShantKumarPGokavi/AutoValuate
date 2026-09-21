import streamlit as st
import pandas as pd
import joblib

# Set page configuration
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# 1. Load trained model and preprocessor artifacts directly from the same folder
@st.cache_resource
def load_artifacts():
    preprocessor = joblib.load('car_preprocessor.pkl')
    model = joblib.load('car_price_model.pkl')
    return preprocessor, model

try:
    preprocessor, model = load_artifacts()
except Exception as e:
    st.error(f"Error loading model artifacts: {e}")
    st.stop()

# 2. Web Application UI Header
st.title("🚗 Used Car Price Predictor")
st.markdown("Provide the vehicle specs below to estimate its current resale value.")

st.divider()

# 3. User Input Form
col1, col2 = st.columns(2)

with col1:
    present_price = st.number_input(
        "Current Ex-Showroom Price (in Lakhs ₹)", 
        min_value=0.1, 
        max_value=100.0, 
        value=5.5, 
        step=0.1
    )
    kms_driven = st.number_input(
        "Kilometers Driven", 
        min_value=0, 
        max_value=500000, 
        value=25000, 
        step=1000
    )
    owner = st.selectbox(
        "Number of Previous Owners", 
        options=[0, 1, 2, 3]
    )

with col2:
    car_age = st.number_input(
        "Age of the Car (in Years)", 
        min_value=0, 
        max_value=30, 
        value=5, 
        step=1
    )
    fuel_type = st.selectbox(
        "Fuel Type", 
        options=['Petrol', 'Diesel', 'CNG']
    )
    seller_type = st.selectbox(
        "Seller Type", 
        options=['Dealer', 'Individual']
    )
    transmission = st.selectbox(
        "Transmission Type", 
        options=['Manual', 'Automatic']
    )

st.divider()

# 4. Prediction Execution
if st.button("Predict Selling Price", type="primary", use_container_width=True):
    input_data = pd.DataFrame([{
        'Present_Price': present_price,
        'Kms_Driven': kms_driven,
        'Owner': owner,
        'Car_Age': car_age,
        'Fuel_Type': fuel_type,
        'Seller_Type': seller_type,
        'Transmission': transmission
    }])

    try:
        processed_input = preprocessor.transform(input_data)
        prediction = model.predict(processed_input)[0]

        st.success(f"### Estimated Resale Price: ₹{prediction:.2f} Lakhs")
    except Exception as e:
        st.error(f"Prediction failed: {e}")