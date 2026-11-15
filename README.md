# Explainable Machine Learning for 10-Year Coronary Heart Disease Risk Prediction

This project uses machine learning to predict the 10-year risk of Coronary Heart Disease (CHD). It uses the Framingham Heart Study dataset.

The project also uses LIME to explain the model's predictions. A Raspberry Pi Pico W simulation is used to show the results on a display.

## Project Overview

The main goal of this project is to build a machine learning system. The system predicts if a person may have coronary heart disease in the next 10 years.

In this project, I tested different ensemble learning algorithms. I also tested different methods for feature scaling and class balancing.

I used a pipeline to prepare the data and train the model. This helped prevent data leakage.

I also used Bayesian Optimization to find better model settings. The F1-score of the positive class was used to select the best settings.

After that, I connected the final model to a Flask API. I used LIME to explain each prediction. The results are also shown on a simulated Raspberry Pi Pico W device.

## Key Features

- **Data preprocessing:** Removing missing values, scaling features, and balancing the data.
- **Ensemble learning:** Testing and comparing different ensemble models.
- **Data leakage prevention:** Using a pipeline for data preparation and model training.
- **Bayesian optimization:** Finding the best model settings.
- **Explainable AI:** Using LIME to explain the model's predictions.
- **Flask API:** Sending data to the model and receiving predictions and explanations.
- **Hardware simulation:** Showing the results on a display using Raspberry Pi Pico W and Wokwi.

## Dataset

This project uses the Framingham Heart Study dataset. It contains health information and different risk factors for coronary heart disease.

- **Target variable:** `TenYearCHD`
- **Prediction task:** Binary classification
- **Features:** Age, smoking habits, blood pressure, cholesterol, glucose, BMI, and other health information.

I removed rows with missing values. I also removed the `education` feature from the dataset.

## Methodology

The project has the following steps:

1. **Data preparation:** Loading the dataset, removing missing values, and separating input features and the target.
2. **Preprocessing:** Testing different feature scaling and class balancing methods.
3. **Model evaluation:** Training and comparing ten ensemble learning algorithms.
4. **Pipeline implementation:** Using a pipeline for preprocessing, sampling, and model training to prevent data leakage.
5. **Hyperparameter optimization:** Using Bayesian Optimization to find the best model settings based on the positive-class F1-score.
6. **Model explainability:** Using LIME to explain individual predictions.
7. **API development:** Connecting the final model to a Flask REST API.
8. **Hardware simulation:** Connecting the API to a Raspberry Pi Pico W simulation with a graphical display in Wokwi.

## Final Model and Results

I selected the final model based on the F1-score of the positive class.

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

The results show a balance between finding positive cases and reducing false-positive predictions.

This model is a prototype for risk prediction and decision support. It is not a medical diagnosis system.

## Hardware Simulation

The final model sends its predictions and LIME explanations to a Raspberry Pi Pico W simulation.

The results are shown on a graphical display.

**Wokwi Simulation:**

[Open the project in Wokwi](https://wokwi.com/projects/440944365735993345)

## Technologies

- Python
- pandas
- NumPy
- scikit-learn
- imbalanced-learn
- Bayesian Optimization
- LIME
- Flask
- REST API
- Postman
- Raspberry Pi Pico W
- Wokwi

## Limitations and Future Work

There are some possible improvements for this project:

- Testing the model with larger and more different medical datasets.
- Testing the model with real patient data from other sources.
- Comparing LIME with other methods, such as SHAP.
- Testing the system with doctors and patients.
- Adding real-time data collection to the hardware system.

## Disclaimer

This project is an academic research prototype.

The results are not medical diagnoses. They should not be used alone to make medical decisions.

## Author

**Mina Farahani**

M.Sc. in Computer Engineering — Computer Architecture

**Academic Supervisor:** Dr. Somayyeh Jafarali Jassbi

**Academic Advisor:** Dr. Mojtaba Hosseini
