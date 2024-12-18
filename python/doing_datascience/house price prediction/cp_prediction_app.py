# app.py

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load("housing_price_model.pkl")

# Streamlit App Title
st.title("🏠 California Housing Price Predictor")

st.write("""
### Enter housing features to predict the median house value.
The prediction is based on the **California Housing Dataset** and a trained Random Forest model.
""")

# Sidebar for user input
st.sidebar.header("Input Features")

# Function to take user input
def user_input_features():
    MedInc = st.sidebar.number_input("Median Income (in 10k USD)", min_value=0.0, max_value=20.0, value=3.0, step=0.1)
    HouseAge = st.sidebar.slider("House Age (in years)", 0, 100, 30)
    AveRooms = st.sidebar.number_input("Average Rooms per House", min_value=1.0, max_value=10.0, value=5.0, step=0.1)
    AveBedrms = st.sidebar.number_input("Average Bedrooms per House", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
    Population = st.sidebar.number_input("Population in Block", min_value=100, max_value=5000, value=1000, step=10)
    AveOccup = st.sidebar.number_input("Average Occupancy per House", min_value=1.0, max_value=10.0, value=3.0, step=0.1)
    Latitude = st.sidebar.number_input("Latitude", min_value=32.0, max_value=42.0, value=37.0, step=0.1)
    Longitude = st.sidebar.number_input("Longitude", min_value=-125.0, max_value=-114.0, value=-120.0, step=0.1)
    
    data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }
    return pd.DataFrame(data, index=[0])

# Get user input
input_df = user_input_features()

# Display user input
st.subheader("User Input Features")
st.write(input_df)

# Make Predictions
prediction = model.predict(input_df)

# Display prediction
st.subheader("Predicted Median House Value")
st.write(f"💰 **${prediction[0] * 100000:.2f}** (USD)")
