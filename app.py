import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('/mnt/c/Users/91911/OneDrive/Desktop/soil-detector-ui/AgriSoilDetector.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Soil Fertility Predictor", layout="centered")
st.title("🌱 Soil Fertility Predictor")
st.markdown("Enter soil nutrient values to predict the fertility category.")

# Input form
with st.form("fertility_form"):
    col1, col2 = st.columns(2)

    with col1:
        N = st.number_input('Nitrogen (N)', min_value=0.0)
        P = st.number_input('Phosphorus (P)', min_value=0.0)
        K = st.number_input('Potassium (K)', min_value=0.0)
        pH = st.number_input('pH Level', min_value=0.0)
        EC = st.number_input('Electrical Conductivity (EC)', min_value=0.0)
    with col2:
        OC = st.number_input('Organic Carbon (OC)', min_value=0.0)
        S = st.number_input('Sulfur (S)', min_value=0.0)
        Zn = st.number_input('Zinc (Zn)', min_value=0.0)
        Fe = st.number_input('Iron (Fe)', min_value=0.0)
        Cu = st.number_input('Copper (Cu)', min_value=0.0)
        Mn = st.number_input('Manganese (Mn)', min_value=0.0)
        Bo = st.number_input('Boron (B)', min_value=0.0)

    submitted = st.form_submit_button("Predict Fertility")

if submitted:
    # Create input dataframe
    input_data = pd.DataFrame([{
        'N': N, 'P': P, 'K': K, 'ph': pH, 'ec': EC, 'oc': OC,
        'S': S, 'zn': Zn, 'fe': Fe, 'cu': Cu, 'Mn': Mn, 'B': Bo
    }])

    # Apply log transformation if required
    input_transformed = input_data.apply(lambda x: np.log10(x + 1e-5) if np.issubdtype(x.dtype, np.number) else x)

    # Predict
    prediction = model.predict(input_transformed)[0]

    # Fertility category mapping
    fertility_map = {
        0: ("🌾 Less Fertile", "Consider using organic compost or micronutrient-rich fertilizers to boost soil productivity."),
        1: ("🌿 Moderately Fertile", "Soil is good, but adding compost and maintaining pH can help sustain fertility."),
        2: ("🌟 Highly Fertile", "Your soil is in excellent condition! Keep rotating crops and avoid over-fertilization.")
    }

    category, suggestion = fertility_map.get(prediction, ("Unknown", "No suggestion available."))

    # Display result
    st.success(f"**Predicted Fertility:** {category}")
    st.info(f"💡 **Suggestion:** {suggestion}")
