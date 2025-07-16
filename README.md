# 🧠 Diabetes Prediction using Machine Learning

A complete machine learning pipeline to predict diabetes using health-related metrics from the Pima Indians Diabetes Dataset. This project is part of the AI summer training program at Modern Academy for Engineering & Technology (2024/2025).

---

## 📌 Overview

Diabetes is a growing health threat worldwide. Early detection is crucial to prevent serious complications. In this project, we use data science and machine learning to build a model that predicts the likelihood of diabetes based on various medical indicators.

---

## 📊 Dataset

- *Source:* [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes)
- *Rows:* 768 samples
- *Features:* 8 health metrics + 1 binary target variable (0: No diabetes, 1: Diabetes)

---

## ⚙ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Seaborn, Matplotlib
- Flask
- SMOTE (from imbalanced-learn)
- Joblib

---

## 🔄 Workflow

```mermaid
graph TD;
    A[Raw Data] --> B[Data Cleaning]
    B --> C[Feature Engineering]
    C --> D[EDA & Visualization]
    D --> E[Model Training]
    E --> F[Model Evaluation]
    F --> G[Model Deployment (Flask API)]
