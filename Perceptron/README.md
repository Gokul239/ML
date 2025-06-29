# 🌸 Iris Classification using Perceptron

A high-level implementation of a **Perceptron-based classifier** applied to the classic **Iris dataset** for multi-class classification. This project demonstrates effective preprocessing, visualization, model training, and evaluation using a simple neural unit — the Perceptron.

---

## 📌 Objective

Build a performant Perceptron model to classify Iris flowers into three species based on morphological features. The goal is to demonstrate how foundational linear models can be effectively applied to multi-class classification with appropriate preprocessing and evaluation.

---

## 🧠 Model Overview

- **Algorithm**: Perceptron (Single-layer Neural Network)
- **Optimizer**: Stochastic Gradient Descent (implicit in Scikit-learn's implementation)
- **Learning Rate**: `eta0 = 0.01`
- **Training Split**: 80% Training / 20% Test (Stratified)

---

## 🗂 Dataset

- **Source**: `sklearn.datasets.load_iris()`
- **Classes**:
  - 0 → Iris Setosa
  - 1 → Iris Versicolor
  - 2 → Iris Virginica
- **Features**:
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)

---

## 🔍 Workflow Summary

1. **Data Loading & Cleansing**
   - Load Iris dataset
   - Convert to DataFrame
   - Handle duplicates, validate nulls

2. **Exploratory Data Analysis**
   - Pairplots for feature interactions
   - Violin & swarm plots for distribution & density analysis

3. **Preprocessing**
   - Normalize features using `StandardScaler` to improve convergence and model performance

4. **Train-Test Split**
   - Stratified sampling to maintain class distribution across train and test sets

5. **Model Training**
   - Train a `Perceptron` model using the normalized features

6. **Evaluation**
   - Accuracy
   - Confusion Matrix
   - Precision & Recall (micro-averaged)

---

## 📈 Metrics & Results

| Metric        | Value (example) |
|---------------|-----------------|
| Accuracy      | ~0.90+          |
| Precision     | micro-average   |
| Recall        | micro-average   |
| Confusion Matrix | Visualized via heatmap |

> Note: Final values may vary slightly due to random state and stratification.

---

## 📊 Visualizations

- **Pairplot**: Multi-dimensional class separation
- **Violin Plot**: Feature distribution by class
- **Swarm Plot**: Individual data point dispersion
- **Heatmap**: Confusion matrix for performance analysis

---

## 💼 Technical Stack

- Python 3.x
- pandas
- seaborn, matplotlib
- scikit-learn

---

## 🚀 Quick Start

### Installation
```bash
pip install pandas scikit-learn seaborn matplotlib
