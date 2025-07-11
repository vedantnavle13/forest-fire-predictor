# 🔥 Forest Fire Prediction Web App

A Flask-based machine learning web application that predicts the risk of forest fire based on environmental features like temperature, humidity, wind speed, and more.

## 🚀 Features

- ML Model: Trained using Ridge Regression.
- Frontend: HTML-based input form.
- Backend: Python + Flask.
- Scaler: StandardScaler for input normalization.
- Model Files: `ridge.pkl` and `scaler.pkl`.

## 📁 Project Structure

├── application.py # Main Flask app
├── modeltraining.ipynb # Notebook to train Ridge model
├── featureseng.ipynb # Feature engineering steps
├── templates/
│ ├── index.html # Home page form
│ └── home.html # Result page
├── ridge.pkl # Saved Ridge model
├── scaler.pkl # Saved Scaler
├── requirements.txt # Python dependencies
├── .gitignore # Files to ignore in Git
└── README.md # You're reading it!


## 📊 Inputs Used for Prediction

- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- FFMC
- DMC
- ISI
- Classes
- Region



