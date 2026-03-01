# 🏦 LoanRisk AI — Intelligent Loan Default Prediction Platform

> A production-grade machine learning system that predicts loan default risk with high recall for financial safety-critical decision making.

---

## 🌟 Product Vision

Financial institutions lose billions annually due to loan defaults.
LoanRisk AI provides a data-driven risk intelligence system that enables lenders to:

* detect high-risk applicants early
* reduce financial losses
* automate credit screening
* support decision-making with predictive analytics

This system is designed as a **deployable fintech product prototype**, not just a model notebook.

---

## 🎯 Problem Statement

Traditional loan approval systems rely on static rules and manual analysis, which:

* miss hidden risk patterns
* fail to scale
* lack predictive intelligence

We solve this using a machine learning-driven decision engine trained on borrower financial and behavioral features.

---

## 💡 Solution

LoanRisk AI is an end-to-end ML system that:

✔ processes raw applicant data
✔ cleans and transforms inputs
✔ predicts default probability
✔ classifies risk level
✔ provides instant decision support

---

## 🧠 Core ML Architecture

**Pipeline Design**

```
Raw Data → Cleaning → Feature Engineering → Scaling → Model → Probability → Risk Decision
```

---

### 📊 Model

| Component          | Choice                  |
| ------------------ | ----------------------- |
| Algorithm          | Logistic Regression     |
| Optimization       | GridSearchCV            |
| Validation         | 5-Fold Cross Validation |
| Metric             | ROC-AUC                 |
| Imbalance Handling | class_weight balancing  |

---

### 📈 Performance

| Metric              | Score    |
| ------------------- | -------- |
| ROC-AUC             | **0.75** |
| Accuracy            | **67%**  |
| Recall (Defaulters) | **70%**  |
| Precision           | **22%**  |

---

### 📌 Why High Recall Matters

In financial risk prediction:

> Missing a defaulter is far worse than flagging a safe applicant.

Therefore, the model is optimized for **risk detection**, not raw accuracy.

---

## 📊 Visual Model Insights

### ROC Curve

Shows strong separation capability between default and non-default classes.

### Feature Importance

Top factors influencing risk prediction:

* Interest Rate
* Loan Amount
* Employment Type
* Credit Lines
* Debt-to-Income Ratio

These match real-world financial risk indicators.

---

## 🖥️ Product Interface

The system includes a responsive web dashboard that allows:

* real-time prediction
* risk visualization
* probability scoring
* instant results

Designed using modern UI principles for fintech-grade usability.

---

## 🏗 System Design

```
User Input → Flask API → Preprocessing → Model → Prediction → UI Output
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Sohel123-png/loan-default-prediction.git
cd loan-default-prediction
pip install -r requirements.txt
python app.py
```

Open:

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
└── README.md
```

---

## 🚀 Innovation Highlights

* Handles high-cardinality features safely
* Prevents memory overflow during encoding
* Uses probability threshold tuning
* Designed for deployment from day one
* Built with production mindset

---

## 🧪 Engineering Challenges Solved

✔ Memory crash during encoding
✔ Dataset imbalance handling
✔ Feature alignment between training & inference
✔ Stable prediction pipeline

---

## 🔮 Future Scope

* Explainable AI dashboard (SHAP)
* Live API endpoint
* Cloud deployment
* Model monitoring system
* Auto-retraining pipeline
* Risk score visualization gauge

---

## 🏆 Why This Project Stands Out

This is **not just a model** — it is a complete ML product prototype demonstrating:

* real-world architecture
* deployment readiness
* problem understanding
* engineering thinking
* product mindset

---

## 👨‍💻 Author

**Sohel Ali**

GitHub
https://github.com/Sohel123-png

LinkedIn
https://www.linkedin.com/in/sayyed-sohel-6435253a8

---

## 📜 License

Educational & portfolio demonstration project.

---

⭐ If this project impressed you, consider starring the repo.
