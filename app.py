import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open('AgriSoilDetector.pkl', 'rb') as file:
    model = pickle.load(file)

# Debug: Show what the model expects
EXPECTED_FEATURES = list(model.feature_names_in_)

st.set_page_config(page_title="Soil Fertility Predictor", layout="centered")
st.title("🌱 Soil Fertility Predictor")
st.markdown("Enter soil nutrient values to predict the fertility category.")

def float_or_none(value):
    try:
        return float(value)
    except:
        return None

def interpret_fertility(level):
    if level == 0:
        return "🟡 **Less Fertile**", "Recommendation: Increase organic matter and consider NPK-rich fertilizers."
    elif level == 1:
        return "🟠 **Moderately Fertile**", "Suggestion: Maintain nutrient levels and monitor soil pH."
    elif level == 2:
        return "🟢 **Highly Fertile**", "Great! Keep monitoring and avoid over-fertilizing."
    else:
        return "Unknown", "No recommendation available."

# Show expected feature names
with st.expander("🔍 See expected feature names by the model"):
    st.write(EXPECTED_FEATURES)

# Input form
with st.form("fertility_form"):
    col1, col2 = st.columns(2)

    with col1:
        N = st.text_input('Nitrogen (N)')
        P = st.text_input('Phosphorus (P)')
        K = st.text_input('Potassium (K)')
        ph = st.text_input('pH Level')
        ec = st.text_input('Electrical Conductivity (EC)')

    with col2:
        oc = st.text_input('Organic Carbon (OC)')
        S = st.text_input('Sulfur (S)')
        zn = st.text_input('Zinc (Zn)')
        fe = st.text_input('Iron (Fe)')
        cu = st.text_input('Copper (Cu)')
        Mn = st.text_input('Manganese (Mn)')
        B = st.text_input('Boron (B)')

    submitted = st.form_submit_button("Predict Fertility")

# On form submit
if submitted:
    inputs = [N, P, K, ph, ec, oc, S, zn, fe, cu, Mn, B]
    converted = list(map(float_or_none, inputs))

    if None in converted:
        st.error("❗ Please fill in all fields with valid numeric values.")
    else:
        # Build dictionary from expected features
        input_data = dict(zip(
            EXPECTED_FEATURES,
            converted
        ))

        input_df = pd.DataFrame([input_data])
        input_transformed = input_df.apply(lambda x: np.log10(x + 1e-5))

        result = model.predict(input_transformed)
        category, recommendation = interpret_fertility(result[0])

        st.subheader("🌾 Predicted Fertility:")
        st.success(category)
        st.markdown(f"📌 {recommendation}")
