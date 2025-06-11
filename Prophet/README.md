# COVID-19 Data Analysis and Forecasting

This project performs exploratory data analysis (EDA) and time series forecasting on a cleaned COVID-19 dataset using Python. It includes data inspection, visualization, and forecasting of confirmed and death cases using **Facebook Prophet**, a powerful model for time series forecasting developed by Meta.

---

## 📁 Files

- `main.ipynb`: The Jupyter notebook containing the full analysis and forecasting pipeline.
- `c_19_clean_ds.csv`: The cleaned COVID-19 dataset (not included — please add this to the same directory before running the notebook).

---

## 📊 Features

### 📌 Data Analysis
- Load and inspect the structure of the COVID-19 dataset.
- Clean and rename columns for consistency.
- Identify the date range and visualize trends in confirmed and death cases.

### 📌 Data Visualization
- Time series plots of confirmed and death cases using Seaborn and Matplotlib.

### 📌 Time Series Forecasting
- Predict confirmed and death case trends using **Facebook Prophet**.
- Evaluate model performance using **Root Mean Squared Error (RMSE)**.
- Forecast COVID-19 death counts for the next 15 days.

---

## 🧠 Forecasting Model: Facebook Prophet

### What is Prophet?
[Facebook Prophet](https://facebook.github.io/prophet/) is an open-source forecasting tool designed for business time series forecasting. It models time series data with:
- **Trend**
- **Seasonality**
- **Holiday effects (optional)**

### How Prophet Works
Prophet fits the following additive model:

y(t) = g(t) + s(t) + h(t) + ε(t)


Where:
- `g(t)` is the trend function (e.g., linear or logistic growth)
- `s(t)` is the seasonality component (weekly, yearly)
- `h(t)` is the effect of holidays or special events
- `ε(t)` is the error term (noise)

### Application in This Project
- Data is grouped by `Date` and renamed to Prophet’s expected format:
  - `ds`: timestamp (datetime)
  - `y`: numeric value (Confirmed or Death cases)
- The dataset is split into training and testing sets for validation.
- Prophet is trained on `Confirmed` case data, and evaluated on the last 5 days using RMSE.
- A 15-day forecast is generated for `Deaths` using the full dataset.

### Model Evaluation
- **RMSE (Root Mean Squared Error)** is used to evaluate the accuracy of the model’s short-term prediction (on the last 5 days of known data).
- This helps validate the model’s generalization before forecasting future values.

---

## 📦 Installation

Install the required packages:

```bash
pip install pandas matplotlib seaborn scikit-learn prophet
