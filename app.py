from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and feature columns
model, feature_columns = pickle.load(open("model/decision_tree_model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Collect raw form data
    input_data = {
        "Age": float(request.form["Age"]),
        "RestingBP": float(request.form["RestingBP"]),
        "Cholesterol": float(request.form["Cholesterol"]),
        "FastingBS": float(request.form["FastingBS"]),
        "MaxHR": float(request.form["MaxHR"]),
        "Oldpeak": float(request.form["Oldpeak"]),
        "Sex": request.form["Sex"],
        "ChestPainType": request.form["ChestPainType"],
        "RestingECG": request.form["RestingECG"],
        "ExerciseAngina": request.form["ExerciseAngina"],
        "ST_Slope": request.form["ST_Slope"],
    }

    # Convert to DataFrame
    df = pd.DataFrame([input_data])

    # One-hot encode to match training
    df_encoded = pd.get_dummies(df)

    # Align input with model feature columns
    df_encoded = df_encoded.reindex(columns=feature_columns, fill_value=0)

    # Predict
    prediction = model.predict(df_encoded)[0]
    result = "High Risk" if prediction == 1 else "Low Risk"

    return render_template("index.html", prediction_text=f"Prediction: {result}")

if __name__ == "__main__":
    app.run(debug=True)
