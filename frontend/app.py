import streamlit as st
import sys
import os
 
# Add backend path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
 
from predict import predict
 
# Page config
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="🫀",
    layout="centered"
)
 
# Custom CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
 
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
 
        .main {
            background-color: #f9f9f9;
        }
 
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 700px;
        }
 
        .header-box {
            background-color: #1a1a2e;
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 2rem;
        }
 
        .header-box h1 {
            color: #ffffff;
            font-size: 1.8rem;
            font-weight: 600;
            margin: 0;
        }
 
        .header-box p {
            color: #a0a0b0;
            font-size: 0.9rem;
            margin-top: 0.4rem;
        }
 
        .section-label {
            font-size: 0.75rem;
            font-weight: 600;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.5rem;
            margin-top: 1.2rem;
        }
 
        div[data-testid="stNumberInput"] input,
        div[data-testid="stSelectbox"] > div {
            border-radius: 8px !important;
            border: 1px solid #e0e0e0 !important;
            background-color: #ffffff !important;
        }
 
        div.stButton > button {
            width: 100%;
            background-color: #1a1a2e;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: 500;
            margin-top: 1.5rem;
            transition: background-color 0.2s ease;
        }
 
        div.stButton > button:hover {
            background-color: #2e2e4e;
            color: white;
        }
 
        .result-box {
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            margin-top: 1.5rem;
            font-size: 1.1rem;
            font-weight: 500;
        }
 
        .result-high {
            background-color: #fff0f0;
            border: 1px solid #ffcccc;
            color: #cc0000;
        }
 
        .result-low {
            background-color: #f0fff4;
            border: 1px solid #b2f5c8;
            color: #1a7a3c;
        }
 
        hr {
            border: none;
            border-top: 1px solid #ececec;
            margin: 1.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)
 
# Header
st.markdown("""
    <div class="header-box">
        <h1>🫀 Heart Disease Prediction</h1>
        <p>Fill in the patient details below to assess cardiovascular risk</p>
    </div>
""", unsafe_allow_html=True)
 
# Section: Personal Info
st.markdown('<div class="section-label">Personal Information</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=20, max_value=100, value=45)
with col2:
    sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
 
st.markdown("<hr>", unsafe_allow_html=True)
 
# Section: Clinical Measurements
st.markdown('<div class="section-label">Clinical Measurements</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", value=120)
    chol = st.number_input("Cholesterol (mg/dl)", value=200)
    thalach = st.number_input("Max Heart Rate Achieved", value=150)
with col4:
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    restecg = st.number_input("Resting ECG Result (0–2)", min_value=0, max_value=2, value=0)
    exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
 
st.markdown("<hr>", unsafe_allow_html=True)
 
# Section: Heart Specifics
st.markdown('<div class="section-label">Heart Specifics</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    cp = st.number_input("Chest Pain Type (0–3)", min_value=0, max_value=3, value=0)
    oldpeak = st.number_input("ST Depression (Oldpeak)", value=1.0, step=0.1)
    ca = st.number_input("Major Vessels (0–3)", min_value=0, max_value=3, value=0)
with col6:
    slope = st.number_input("Slope of ST Segment (0–2)", min_value=0, max_value=2, value=1)
    thal = st.number_input("Thalassemia (0–3)", min_value=0, max_value=3, value=2)
 
# Predict Button
if st.button("Analyse Risk"):
    input_data = [
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach, exang,
        oldpeak, slope, ca, thal
    ]
 
    result = predict(input_data)
 
    if result == 1:
        st.markdown("""
            <div class="result-box result-high">
                ⚠️ High Risk of Heart Disease Detected<br>
                <span style="font-size:0.85rem; font-weight:400;">Please consult a cardiologist for further evaluation.</span>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="result-box result-low">
                ✅ Low Risk — No Immediate Concern<br>
                <span style="font-size:0.85rem; font-weight:400;">Continue maintaining a healthy lifestyle.</span>
            </div>
        """, unsafe_allow_html=True)
 
# Footer
st.markdown("""
    <div style="text-align:center; color:#bbb; font-size:0.75rem; margin-top:3rem;">
        This tool is for educational purposes only and not a substitute for medical advice.
    </div>
""", unsafe_allow_html=True)