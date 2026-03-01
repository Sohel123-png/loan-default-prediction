from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# --- Configuration & Asset Loading ---
MODEL_PATH = "log_regression.pkl"
SCALER_PATH = "scaler.pkl"
# These names must match the categorical columns in your CSV exactly
CAT_FEATURES = [
    "Education", "EmploymentType", "MaritalStatus", 
    "HasMortgage", "HasDependents", "LoanPurpose", "HasCoSigner"
]

def load_ml_assets():
    """Loads the model, scaler, and all categorical encoders."""
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        # Load all 7 encoders into a dictionary
        encoders = {feat: joblib.load(f"{feat}_encoder.pkl") for feat in CAT_FEATURES}
        return model, scaler, encoders
    except FileNotFoundError as e:
        print(f"Error: Missing ML files. Did you run the notebook? {e}")
        return None, None, None

model, scaler, encoders = load_ml_assets()

# Business Logic: Adjusted threshold for high-risk detection
THRESHOLD = 0.11 

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    error_message = None

    if request.method == "POST":
        try:
            # 1. Extract Numerical Data from Form
            # Order must match the training set: Age, Income, LoanAmount, etc.
            num_values = [
                float(request.form["Age"]),
                float(request.form["Income"]),
                float(request.form["LoanAmount"]),
                float(request.form["CreditScore"]),
                float(request.form["MonthsEmployed"]),
                float(request.form["NumCreditLines"]),
                float(request.form["InterestRate"]),
                float(request.form["LoanTerm"]),
                float(request.form["DTIRatio"])
            ]

            # 2. Extract and Encode Categorical Data
            cat_values = []
            for feat in CAT_FEATURES:
                raw_val = request.form[feat].strip().lower()
                # Use the loaded encoder for this specific feature
                encoded_val = encoders[feat].transform([raw_val])[0]
                cat_values.append(encoded_val)

            # 3. Combine and Reshape for Prediction
            # Final array shape: [[num1, num2... cat1, cat2...]]
            input_data = np.array([num_values + cat_values])

            # 4. Scale the input
            input_scaled = scaler.transform(input_data)

            # 5. Predict Probability
            prob = model.predict_proba(input_scaled)[0][1]
            
            # 6. Apply Custom Threshold
            prediction = 1 if prob > THRESHOLD else 0
            probability = f"{round(prob * 100, 2)}%"

        except Exception as e:
            error_message = f"Incomplete or Invalid Input: {str(e)}"
            print(f"Prediction error: {e}")

    return render_template(
        "index.html", 
        prediction=prediction, 
        probability=probability,
        error=error_message
    )

if __name__ == "__main__":
    # Ensure assets are loaded before starting server
    if model and scaler:
        app.run(debug=True)
    else:
        print("Flask server aborted: ML assets not found.")