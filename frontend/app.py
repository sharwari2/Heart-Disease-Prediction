import streamlit as st
import sys
import os

# Add backend path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from predict import predict

st.title("❤️ Heart Disease Prediction")

st.write("Enter patient details:")

# Inputs (based on your dataset columns)
age = st.number_input("Age", 20, 100)
sex = st.selectbox("Sex (0=Female,1=Male)", [0,1])
cp = st.number_input("Chest Pain Type", 0, 3)
trestbps = st.number_input("Resting BP")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1])
restecg = st.number_input("Rest ECG", 0, 2)
thalach = st.number_input("Max Heart Rate")
exang = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("Oldpeak")
slope = st.number_input("Slope", 0, 2)
ca = st.number_input("Num Major Vessels", 0, 3)
thal = st.number_input("Thal", 0, 3)

if st.button("Predict"):
    input_data = [
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach, exang,
        oldpeak, slope, ca, thal
    ]
    
    result = predict(input_data)
    
    if result == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk")