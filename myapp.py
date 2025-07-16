import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("./models/SVC.pkl")

# Page title
st.title("Diabetes Prediction App")

# Input form
st.sidebar.header("Enter Patient Data")

def user_input():
    Pregnancies = st.sidebar.number_input("Pregnancies", 0, 20, 1)
    Glucose = st.sidebar.slider("Glucose", 0, 200, 120)
    BloodPressure = st.sidebar.slider("Blood Pressure", 0, 140, 70)
    SkinThickness = st.sidebar.slider("Skin Thickness", 0, 100, 20)
    Insulin = st.sidebar.slider("Insulin", 0, 850, 80)
    BMI = st.sidebar.slider("BMI", 0.0, 70.0, 25.0)
    DiabetesPedigreeFunction = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    Age = st.sidebar.slider("Age", 10, 100, 33)

    data = {
        'Pregnancies': Pregnancies,
        'Glucose': Glucose,
        'BloodPressure': BloodPressure,
        'SkinThickness': SkinThickness,
        'Insulin': Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': Age
    }
    return pd.DataFrame([data])

input_df = user_input()

st.subheader("Patient Data Input")
st.write(input_df)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    pred_proba = model.predict_proba(input_df)[0][prediction]

    if prediction == 1:
        st.error(f"Prediction: Patient is likely diabetic ({pred_proba:.2%} confidence)")
    else:
        st.success(f"Prediction: Patient is not diabetic ({pred_proba:.2%} confidence)")
