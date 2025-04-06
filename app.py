import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
with open('AgriSoilDetector.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit page config
st.set_page_config(page_title="Soil Fertility Predictor", layout="centered")
st.title("🌱 Soil Fertility Predictor")
st.markdown("Enter soil nutrient values to predict the fertility category.")

# Helper: Try convert to float, return None if invalid
def float_or_none(value):
    try:
        return float(value)
    except:
        return None

# Helper: Interpret model output
def interpret_fertility(level):
    if level == 0:
        return "🟡 **Less Fertile**", "Recommendation: Increase organic matter and consider NPK-rich fertilizers."
    elif level == 1:
        return "🟠 **Moderately Fertile**", "Suggestion: Maintain nutrient levels and monitor soil pH."
    elif level == 2:
        return "🟢 **Highly Fertile**", "Great! Keep monitoring and avoid over-fertilizing."
    else:
        return "Unknown", "No recommendation available."

# Input Form UI
with st.form("fertility_form"):
    col1, col2 = st.columns(2)

    with col1:
        N = st.text_input('Nitrogen (N)', value="")
        P = st.text_input('Phosphorus (P)', value="")
        K = st.text_input('Potassium (K)', value="")
        pH = st.text_input('pH Level', value="")
        EC = st.text_input('Electrical Conductivity (EC)', value="")

    with col2:
        OC = st.text_input('Organic Carbon (OC)', value="")
        S = st.text_input('Sulfur (S)', value="")
        Zn = st.text_input('Zinc (Zn)', value="")
        Fe = st.text_input('Iron (Fe)', value="")
        Cu = st.text_input('Copper (Cu)', value="")
        Mn = st.text_input('Manganese (Mn)', value="")
        Bo = st.text_input('Boron (B)', value="")

    submitted = st.form_submit_button("Predict Fertility")

# Prediction
if submitted:
    inputs = [N, P, K, pH, EC, OC, S, Zn, Fe, Cu, Mn, Bo]
    converted = list(map(float_or_none, inputs))

    if None in converted:
        st.error("❗ Please fill in all fields with valid numeric values.")
    else:
        # Convert inputs
        N, P, K, pH, EC, OC, S, Zn, Fe, Cu, Mn, Bo = converted

        # Prepare DataFrame
        input_df = pd.DataFrame([{
            'N': N, 'P': P, 'K': K, 'pH': pH, 'EC': EC, 'OC': OC,
            'S': S, 'zn': Zn, 'fe': Fe, 'cu': Cu, 'Mn': Mn, 'B': Bo
        }])


        # Apply log transform
        input_transformed = input_df.apply(lambda x: np.log10(x + 1e-5))

        # Predict
        result = model.predict(input_transformed)
        category, recommendation = interpret_fertility(result[0])

        # Display result
        st.subheader("🌾 Predicted Fertility:")
        st.success(category)
        st.markdown(f"📌 {recommendation}")
