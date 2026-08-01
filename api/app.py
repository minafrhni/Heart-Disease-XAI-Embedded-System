"""
Flask REST API for Explainable Coronary Heart Disease Prediction

This API loads the Framingham dataset, trains the machine learning
pipeline, predicts the 10-year risk of Coronary Heart Disease (CHD),
and returns both the prediction probability and a LIME explanation.
"""

from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SVMSMOTE
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from lime.lime_tabular import LimeTabularExplainer


# ============================================================
# Load and prepare the dataset
# ============================================================
df= pd.read_csv("Framingham.csv")
df.dropna(inplace=True)

x= df.drop(['education', 'TenYearCHD'], axis=1)
y= df['TenYearCHD']

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.3, random_state= 42)


# ============================================================
# Build the machine learning pipeline
# ============================================================
model= Pipeline([
    ('scaler', StandardScaler()),
    ('sampler', SVMSMOTE(random_state= 42)),
    ('clf', GradientBoostingClassifier(
        n_estimators= 91,
        learning_rate= 0.0943955594307824,
        max_depth= 1,
        min_samples_split= 13,
        min_samples_leaf= 18,
        subsample= 0.6956603764461835,
        random_state= 42
    ))  ]).fit(x_train, y_train)


# ============================================================
# Initialize the LIME explainer
# ============================================================
explainer= LimeTabularExplainer(
    training_data= np.array(x_train),
    feature_names= x_train.columns,
    class_names= ['NoCHD', 'CHD'],
    mode= 'classification')


# ============================================================
# Create the Flask application
# ============================================================
app= Flask(__name__)


# ============================================================
# Prediction endpoint
# ============================================================
@app.route("/predict", methods= ["POST"])
def predict():
    """
    Accepts a patient's clinical data and returns:
        - Predicted CHD probability
        - LIME explanation
    """
        
    try:
        data = request.json.get("data", None)

        # Validate input
        if data is None or len(data) != 14:
            return jsonify({"error": "Input data must be a list of length 14"}), 400

        # Replace missing values with zero
        clean = [0 if v is None else v for v in data]

        # Convert input to DataFrame
        arr = pd.DataFrame([clean], columns=x_train.columns)

        # Predict CHD probability
        probability = round(model.predict_proba(arr)[0][1] * 100, 2)

        # Generate local explanation using LIME
        exp = explainer.explain_instance(
            data_row=arr.iloc[0],
            predict_fn=model.predict_proba,
            num_features=14)

        lime_features = []
        for feature, weight in exp.as_list():
            lime_features.append({
                "feature": feature,
                "weight": weight * 100
            })

        return jsonify({
            "probability": probability,
            "lime_features": lime_features
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ============================================================
# Run the API
# ============================================================
if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 7860, debug= False)