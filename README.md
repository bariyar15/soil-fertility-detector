# 🌱 Soil Fertility Predictor

Welcome to the **Soil Fertility Predictor** — a web-based app built using **Streamlit** and **Machine Learning** to help farmers, researchers, and agricultural officers assess the fertility of soil based on key nutrient values.

---

## 🚀 Features

- 🔍 **Easy Input Interface** for soil nutrient values
- 🤖 **ML-Based Predictions** of soil fertility (Less Fertile / Moderately Fertile / Highly Fertile)
- 📊 **Log-transformation preprocessing** as used in model training
- 💡 **Suggestions for improvement** based on fertility levels
- 🌐 Deployable online with **Streamlit Cloud**

---

## 🧪 Inputs

The app takes the following soil nutrient values as input:

| Parameter | Description              |
|----------|---------------------------|
| N        | Nitrogen (ppm)            |
| P        | Phosphorus (ppm)          |
| K        | Potassium (ppm)           |
| pH       | Soil pH                   |
| EC       | Electrical Conductivity   |
| OC       | Organic Carbon            |
| S        | Sulfur                    |
| Zn       | Zinc                      |
| Fe       | Iron                      |
| Cu       | Copper                    |
| Mn       | Manganese                 |
| B        | Boron                     |

---

## 🧠 Model

- The backend is powered by a trained **Random Forest Classifier**.
- Input values are **log-transformed** before prediction to match training data preprocessing.

---

## 📈 Output Categories

| Class | Fertility Level     | Suggestion |
|-------|----------------------|------------|
| 0     | ❌ Less Fertile      | Add organic matter, optimize NPK balance |
| 1     | ⚠ Moderately Fertile | Supplement with micronutrients and monitor EC |
| 2     | ✅ Highly Fertile    | Maintain current practices and monitor regularly |

---

## 📦 Installation

Clone the repo and install dependencies:
```bash
git clone https://github.com/bariyar15/soil-fertility-predictor.git
cd soil-fertility-predictor
pip install -r requirements.txt
