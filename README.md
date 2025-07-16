
# 🧠 Diabetes Prediction using Machine Learning

A complete machine learning pipeline to predict diabetes using health-related metrics from the Pima Indians Diabetes Dataset. This project is part of the AI summer training program at Modern Academy for Engineering & Technology (2024/2025).

---

## 📌 Overview

Diabetes is a growing health threat worldwide. Early detection is crucial to prevent serious complications. In this project, we use data science and machine learning to build a model that predicts the likelihood of diabetes based on various medical indicators.

---

## 📊 Dataset

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes)
- **Rows:** 768 samples
- **Features:** 8 health metrics + 1 binary target variable (0: No diabetes, 1: Diabetes)

---

## ⚙️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Seaborn, Matplotlib
- Flask
- SMOTE (from imbalanced-learn)
- Joblib

---

## 🔄 Workflow

```graph TD;
  A[Raw Data] --> B[Data Cleaning]
  B --> C[Feature Engineering]
  C --> D[EDA & Visualization]
  D --> E[Model Training]
  E --> F[Model Evaluation]
  F --> G["Model Deployment (Flask API)"]
```

---

## 🔬 Exploratory Data Analysis (EDA)

- ✅ Histograms and boxplots for distributions
- ✅ Correlation heatmaps and PCA
- ✅ Outlier detection and treatment
- ✅ Class imbalance handled using SMOTE

---

## 🧪 Model Training

Trained and evaluated:
- Logistic Regression
- Decision Tree
- Random Forest
- SVM
- KNN
- MLP (Neural Network)

🧠 **Best Model**: Random Forest (after GridSearchCV tuning)

---

## 📈 Performance Metrics

| Metric      | Score     |
|-------------|-----------|
| Accuracy    | ~0.85     |
| Precision   | ~0.82     |
| Recall      | ~0.87     |
| F1-Score    | ~0.84     |
| ROC-AUC     | ~0.90     |

*(Exact values may vary slightly with re-training.)*

---

## 🚀 API Deployment

Model deployed using **Flask** as a REST API.

**Endpoint:** `/predict`  
**Method:** POST  
**Payload Example:**
```json
{
  "features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]
}
```
**Response:**
```json
{
  "prediction": 1
}
```

---

## 🧑💻 Team Members

- **Pola Fawzy** (2020) – 4240405  
- **Ahmad Elsaid** (2020) – 4220128  
- **Mohamed Abdelrhman** (2020) – 4220196  

> Modern Academy for Engineering & Technology  
> AI Summer Training 2024/2025

---

## 📌 Future Improvements

- Add frontend (Streamlit or React)
- Use more complex models (XGBoost, LSTM)
- Integrate with real-time medical data systems
- Address potential model bias and ethics

---

## 📎 License

This project is for academic use only.  
Contact us for permissions or collaborations.

