import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("Random Forest Classifier.pkl") 


# App title
st.set_page_config(page_title="🩺 Diabetes Prediction App", layout="centered")
st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details below to predict the likelihood of diabetes.")


# User input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=3)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=32.0, format="%.2f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.47, format="%.3f")
age = st.number_input("Age", min_value=21, max_value=100, value=33)
insulin_missing = 1 if insulin == 0 else 0

# Collect inputs into array
features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age,insulin_missing]])

# Predict
if st.button("Predict"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.error(f"⚠️ The model predicts: **Diabetes Positive** (Risk: {probability:.2f})")
    else:
        st.success(f"✅ The model predicts: **Diabetes Negative** (Risk: {probability:.2f})")

