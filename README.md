# Heart Disease XAI Embedded System

An end-to-end **Explainable Artificial Intelligence (XAI)** system for predicting the **10-year risk of Coronary Heart Disease (CHD)** and deploying the prediction on an embedded platform using **Raspberry Pi Pico W**.

This project was developed as part of my **M.Sc. thesis in Computer Engineering** and integrates **Machine Learning**, **Explainable AI**, **REST APIs**, and **Embedded Systems** into a single working prototype.

---

## Overview

Traditional machine learning models can produce accurate predictions but often fail to explain how those predictions are made. In healthcare applications, interpretability is essential because clinicians need to understand the reasoning behind an AI model before trusting its recommendations.

This project addresses this challenge by combining a machine learning model with **LIME (Local Interpretable Model-Agnostic Explanations)** to provide transparent predictions for coronary heart disease risk.

The trained model is deployed as a **Flask REST API**, while a **Raspberry Pi Pico W** running **MicroPython** collects patient information, sends it to the API via Wi-Fi, and displays both the prediction and its explanation on an **ILI9341 TFT display**.

The embedded hardware prototype was developed and simulated using **Wokwi**.

---

## Project Demonstration

A short demonstration of the complete system running in Wokwi.

The video shows:

- Connecting the Raspberry Pi Pico W to Wi-Fi
- Entering patient information using the keypad
- Sending data to the Flask REST API
- Receiving the CHD prediction
- Displaying the LIME explanation on the TFT display

Watch the demonstration video here:

https://github.com/minafrhni/Heart-Disease-XAI-Embedded-System/issues/1

---

## Key Features

- Predicts the **10-year risk of Coronary Heart Disease (CHD)**
- Uses the **Framingham Heart Study Dataset**
- Handles class imbalance using **SVMSMOTE**
- Applies **StandardScaler** for feature normalization
- Uses a **Gradient Boosting Classifier**
- Optimizes hyperparameters with **Bayesian Optimization**
- Maximizes the **F1-score of the positive (CHD) class**
- Generates prediction explanations using **LIME**
- Deploys the trained model through a **Flask REST API**
- Demonstrates embedded AI deployment using **Raspberry Pi Pico W**
- Supports keypad-based patient data entry
- Displays color-coded feature importance on an **ILI9341 TFT display**

---

## System Architecture

```text
                 Patient
                    │
                    ▼
      Raspberry Pi Pico W (MicroPython)
                    │
               Wi-Fi Request
                    │
                    ▼
            Flask REST API
                    │
                    ▼
      Machine Learning Pipeline
                    │
                    ▼
     StandardScaler → SVMSMOTE
                    │
                    ▼
    Gradient Boosting Classifier
                    │
                    ▼
        CHD Risk Prediction
                    │
                    ▼
         LIME Explanation
                    │
                    ▼
            JSON Response
                    │
                    ▼
        ILI9341 TFT Display
```

---

## Machine Learning Pipeline

The prediction model consists of the following stages:

1. Missing value removal
2. Feature scaling using **StandardScaler**
3. Class balancing using **SVMSMOTE**
4. Classification using **Gradient Boosting**
5. Hyperparameter optimization using **Bayesian Optimization**
6. Local explanation generation using **LIME**

The optimization objective was to maximize the **F1-score of the positive (CHD) class**, providing a better balance between Precision and Recall for the minority class.

---

## Explainable AI

Unlike conventional prediction systems, this project also explains **why** a prediction was made.

For every patient, the API returns:

- Predicted probability of CHD
- Most influential clinical features
- Positive and negative feature contributions

Example:

```json
{
  "probability": 11.17,
  "lime_features": [
    {
      "feature": "age <= 42",
      "weight": -25.17
    },
    {
      "feature": "glucose > 87",
      "weight": 2.45
    }
  ]
}
```

Positive weights indicate an increase in predicted risk, while negative weights indicate a reduction in predicted risk.

---

## Embedded Hardware

The embedded interface was implemented using **MicroPython** and simulated in **Wokwi**.

### Hardware Components

- Raspberry Pi Pico W
- ILI9341 TFT Display
- 4×4 Matrix Keypad

### Embedded Workflow

1. Collect patient information through the keypad.
2. Send the collected data to the Flask API.
3. Receive the predicted CHD probability.
4. Receive the LIME explanation.
5. Display the prediction and feature importance on the TFT display.

---

## Project Structure

```text
Heart-Disease-XAI-Embedded-System
│
├── api
│   ├── app.py
│   ├── requirements.txt
│   └── Framingham.csv
│
├── hardware
│   ├── main.py
│   ├── ili9341.py
│   └── diagram.json
│
└── README.md
```

---

## Dataset

**Framingham Heart Study Dataset**

https://www.kaggle.com/datasets/aasheesh200/framingham-heart-study-dataset

---

## Wokwi Simulation

The complete embedded prototype can be viewed here:

https://wokwi.com/projects/440944365735993345

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Heart-Disease-XAI-Embedded-System.git
```

Install the required packages:

```bash
cd api
pip install -r requirements.txt
```

Run the Flask API:

```bash
python app.py
```

Update the API URL inside **hardware/main.py** and run the project in **Wokwi**.

---

## Technologies

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Imbalanced-learn
- Bayesian Optimization
- LIME
- MicroPython
- Raspberry Pi Pico W
- Wokwi
- REST API

---

## Future Work

- Integrate SHAP alongside LIME
- Deploy the system on physical Raspberry Pi Pico W hardware
- Replace LocalTunnel with a cloud deployment solution
- Improve the embedded graphical interface
- Add patient history management
- Evaluate additional ensemble learning algorithms

---

## Disclaimer

This project was developed for **research and educational purposes only**.

It is **not** a certified medical diagnostic system and should **not** be used as a substitute for professional medical judgment.

---

## Author

**Mina F. Farahani**

M.Sc. in Computer Engineering

### Research Interests

- Explainable Artificial Intelligence (XAI)
- Machine Learning
- Healthcare AI
- Embedded Systems
- Internet of Things (IoT)
