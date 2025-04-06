# Linear Regression Analysis

This project demonstrates a simple linear regression pipeline using Python and common data science libraries. The goal is to explore and model the relationship between independent variables and a target variable using a real-world dataset.

## 📂 Project Structure

- `main.ipynb` - Jupyter notebook containing the entire workflow: data preprocessing, modeling, and evaluation.
- `linear regression.csv` - Dataset used for analysis (ensure this file is present in the working directory).

## 📊 Features

- Data cleaning and preprocessing
- Label encoding for categorical variables
- Multicollinearity check using Variance Inflation Factor (VIF)
- Linear regression modeling using `scikit-learn`
- Model evaluation using:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R-squared (R²)

## 🛠️ Dependencies

Make sure you have the following Python packages installed:

```bash
pip install pandas matplotlib seaborn scikit-learn statsmodels
