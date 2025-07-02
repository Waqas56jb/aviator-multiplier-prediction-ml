# Aviator Multiplier Prediction

Predict the next multiplier in the Aviator game based on previous game statistics using machine learning models. This project includes data analysis, model training, evaluation, and a user-friendly web interface built with Flask for real-time multiplier prediction.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Dataset](#dataset)  
- [Modeling Approach](#modeling-approach)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Results & Visualizations](#results--visualizations)  
- [Contributing](#contributing)  
- [Credits](#credits)  
- [License](#license)

---

## Project Overview

Aviator is an online game where players bet on multipliers that increase over time until a random crash occurs. This project aims to predict the upcoming multipliers based on historical game data using regression machine learning models.

The solution involves:

- Cleaning and exploratory data analysis (EDA) on the Aviator dataset  
- Feature engineering based on game statistics  
- Training multiple regression models (Random Forest, Gradient Boosting, KNN, etc.)  
- Evaluating models using metrics like MSE, MAE, R² and visualizing results  
- Deploying the best model using a Flask web app with a polished UI for interactive prediction

---

## Features

- Data preprocessing and detailed exploratory data analysis with insightful visualizations  
- Implementation of multiple regression models with hyperparameter tuning  
- Comprehensive model evaluation and comparison using plots and metrics  
- RESTful Flask server hosting the prediction model with a clean, responsive UI  
- User inputs game features and receives real-time multiplier predictions  
- Model persistence with joblib for fast, scalable deployment  

---

## Dataset

The dataset contains historical Aviator game records with the following key features:

- `color`: Binary indicator of color (0 or 1)  
- `mean`: Mean value of recent multipliers  
- `var`: Variance of multipliers  
- `next_approximate`: Approximate next multiplier value  
- `target`: Actual multiplier value to predict

Dataset size: ~15.4MB (original source: [Kaggle Aviator Dataset](https://www.kaggle.com/))

---

## Modeling Approach

- Data split into training, validation, and test sets with stratification  
- Feature scaling with StandardScaler inside sklearn Pipelines  
- Models used:
  - Random Forest Regressor  
  - Gradient Boosting Regressor  
  - K-Nearest Neighbors Regressor  
  - Linear Regression  
  - AdaBoost Regressor  
- Evaluation metrics:
  - Mean Squared Error (MSE)  
  - Mean Absolute Error (MAE)  
  - R-squared (R²)  
- Visualization of feature importance, residuals, and model comparison plots  
- Best model selection based on validation set performance

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aviator-multiplier-prediction.git
   cd aviator-multiplier-prediction
