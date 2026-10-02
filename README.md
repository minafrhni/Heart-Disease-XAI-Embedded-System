# Explainable Machine Learning for 10-Year Coronary Heart Disease Risk Prediction

An explainable machine learning system for predicting the 10-year risk of coronary heart disease (CHD) using the Framingham Heart Study dataset. The project combines ensemble learning, Bayesian hyperparameter optimization, LIME-based explanations, and a Raspberry Pi Pico W hardware simulation.

## Project Overview

The main objective of this project is to develop a machine learning system that estimates an individual's risk of developing coronary heart disease within the next 10 years.

Multiple ensemble learning algorithms were evaluated using different feature-scaling and class-balancing techniques. To improve model reliability and prevent data leakage, preprocessing and model training were integrated into a pipeline. Bayesian optimization was then applied to tune model hyperparameters, with the F1-score of the positive (patient) class as the optimization objective.

The selected model was integrated into a Flask API and connected to a simulated hardware interface. LIME was used to provide local explanations for individual predictions.

## Key Features

* **Data preprocessing:** Handling missing values, feature scaling, and class-imbalance techniques.
* **Ensemble learning:** Evaluation and comparison of multiple ensemble classifiers.
* **Data leakage prevention:** Using pipelines to ensure preprocessing is fitted only on training data.
* **Bayesian optimization:** Hyperparameter tuning to improve model performance.
* **Explainable AI:** Using LIME to identify features influencing individual predictions.
* **Flask API:** Serving predictions and explanations through a REST API.
* **Hardware simulation:** Displaying prediction results and explanations using a Raspberry Pi Pico W and a graphical display in Wokwi.

## Dataset

The project uses the Framingham Heart Study dataset, which contains demographic and medical risk factors associated with coronary heart disease.

* **Target variable:** `TenYearCHD`
* **Prediction task:** Binary classification
* **Features:** Demographic and clinical risk factors, including age, smoking habits, blood pressure, cholesterol, glucose, and BMI.

Records with missing values were removed, and the `education` feature was excluded during model development.

## Methodology

The project followed these main steps:

1. **Data preparation:** Loading the dataset, handling missing values, and separating features from the target variable.
2. **Preprocessing:** Evaluating different feature-scaling and class-balancing methods.
3. **Model evaluation:** Training and comparing ten ensemble learning algorithms.
4. **Pipeline implementation:** Integrating preprocessing, sampling, and model training to prevent data leakage.
5. **Hyperparameter optimization:** Applying Bayesian optimization to maximize the positive-class F1-score.
6. **Model explainability:** Using LIME to generate local explanations for predictions.
7. **API development:** Deploying the selected model through a Flask REST API.
8. **Hardware simulation:** Connecting the prediction service to a Raspberry Pi Pico W simulation with a graphical display.

## Final Model and Results

The final model was selected based on the F1-score of the positive (patient) class.

| Component                   | Selected Method                |
| --------------------------- | ------------------------------ |
| Classifier                  | GradientBoostingClassifier     |
| Feature scaling             | StandardScaler                 |
| Sampling method             | SVMSMOTE                       |
| Hyperparameter optimization | Bayesian Optimization          |
| Explainability              | LIME                           |
| API framework               | Flask                          |
| Hardware simulation         | Raspberry Pi Pico W with Wokwi |

### Test Set Performance

| Metric                     | Score |
| -------------------------- | ----: |
| Accuracy                   |  0.76 |
| Precision (positive class) |  0.35 |
| Recall (positive class)    |  0.58 |
| F1-score (positive class)  |  0.44 |

The results reflect a trade-off between identifying positive cases and limiting false-positive predictions. The model is intended as a risk-prediction and decision-support prototype, not as a replacement for professional medical assessment.

## Hardware Simulation

The selected model's predictions and LIME explanations are presented through a simulated hardware interface built with a Raspberry Pi Pico W and a graphical display.

**Wokwi Simulation:**
[Open the project in Wokwi](https://wokwi.com/projects/440944365735993345)

## Technologies

* Python
* pandas
* NumPy
* scikit-learn
* imbalanced-learn
* Bayesian optimization
* LIME
* Flask
* REST API
* Postman
* Raspberry Pi Pico W
* Wokwi

## Repository Contents

The repository contains the final implementation files, model-related code, and resources required to understand and reproduce the project. Refer to the source files for implementation details and execution instructions.

## Limitations and Future Work

* Evaluating the model on larger and more diverse clinical datasets.
* Conducting external validation using real-world patient data.
* Comparing LIME with other explainability methods, such as SHAP.
* Evaluating the usability and reliability of the system in clinical settings.
* Extending the hardware prototype to support real-time data acquisition.

## Disclaimer

This project is an academic research prototype. Its predictions are not medical diagnoses and should not be used as the sole basis for clinical decisions.

## Author

**Mina Farahani**
M.Sc. in Computer Engineering — Computer Architecture
