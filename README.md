# 🏦 Loan Default Prediction System

> A production-ready Machine Learning web application that predicts loan default risk using financial and demographic data.

---

## 🚀 Overview

This project builds an end-to-end machine learning pipeline that predicts whether a loan applicant is likely to default.
It demonstrates **real-world ML workflow**, including preprocessing, model optimization, evaluation, and deployment through a Flask web interface.

The system is designed to simulate how financial institutions assess lending risk using predictive analytics.

---

## 🧠 Tech Stack

**Languages & Frameworks**

* Python
* Flask
* HTML / CSS

**Machine Learning**

* Scikit-learn
* Logistic Regression
* GridSearchCV
* ROC-AUC Optimization

**Libraries**

* NumPy
* Pandas
* Matplotlib
* Joblib

---

## ⚙️ Machine Learning Pipeline

### 🔹 Data Preprocessing

* Removed duplicate entries
* Dropped high-cardinality identifier column (`LoanID`)
* Filled missing values
* Applied IQR-based outlier treatment
* Encoded categorical features
* Standardized numerical features

---

### 🔹 Model Training

* Logistic Regression classifier
* Class imbalance handled using `class_weight="balanced"`
* Hyperparameter tuning with **GridSearchCV**
* 5-fold cross-validation
* Optimized using ROC-AUC score

---

### 🔹 Evaluation Metrics

* Classification Report
* Confusion Matrix
* ROC Curve
* Precision-Recall Curve
* Feature Importance Analysis

---

## 📊 Model Performance

The model was evaluated using standard classification metrics on unseen test data.

| Metric                    | Score    |
| ------------------------- | -------- |
| Accuracy                  | **67%**  |
| ROC-AUC                   | **0.75** |
| Precision (Default Class) | **0.22** |
| Recall (Default Class)    | **0.70** |
| F1 Score (Default Class)  | **0.33** |

---

### 📈 Performance Interpretation

* The model successfully detects **70% of actual defaulters**, making it effective for risk detection.
* Lower precision indicates the model intentionally prioritizes **recall over precision**, which is suitable for financial risk systems where missing a defaulter is more costly than false alerts.
* ROC-AUC score of **0.75** indicates good class separation capability.

---

### 🎯 Why This Model Is Useful

In loan risk prediction:

> It is safer to incorrectly flag a safe applicant
> than to miss a risky borrower.

This model is optimized accordingly.

---

### 📊 Class Distribution Insight

| Class | Meaning     | Count  |
| ----- | ----------- | ------ |
| 0     | Non-Default | 45,139 |
| 1     | Default     | 5,931  |

The dataset is **imbalanced**, and this was handled using:

* class weighting
* ROC-based threshold tuning

---

### 🧠 Key Observation

This model is tuned for **risk-sensitive prediction**, not raw accuracy.

Financial institutions prefer:

> High recall for defaulters > High accuracy

which this model achieves successfully.


## 🌐 Web Application Features

The deployed Flask interface allows users to:

* Enter financial details
* Select applicant attributes
* Get real-time prediction
* View probability score
* Assess risk category

The interface is designed with a modern responsive UI for better usability.

---

## 🖥️ Installation Guide

Clone repository:

```bash
git clone https://github.com/your-username/loan-default-prediction.git
cd loan-default-prediction
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

---

## 📂 Project Structure

```
loan-default-prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── columns.pkl
│
├── templates/
│   └── index.html
│
├── notebooks/
│   └── model_training.ipynb
│
├── requirements.txt
└── README.md
```

---

## 📈 Future Improvements

* Convert pipeline into sklearn Pipeline object
* Add SHAP explainability dashboard
* Deploy on cloud platform
* Add prediction logging system
* Implement real-time monitoring

---

## 🎯 Learning Outcomes

This project demonstrates strong understanding of:

* Feature engineering
* Handling high-cardinality features
* Preventing memory overflow
* Model evaluation techniques
* Threshold optimization
* Production-ready deployment

---

## 👨‍💻 Author

**Sohel Ali**

* GitHub → https://github.com/Sohel123-png
* LinkedIn →[ https://linkedin.com/in/your-profile](https://www.linkedin.com/in/sayyed-sohel-6435253a8?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

## 📜 License

This project is created for educational and portfolio demonstration purposes.

---

⭐ If you found this project useful, consider starring the repository.

