# 🏏 Player Performance Clustering Using K-Means

This project aims to preprocess and cluster cricket player performance data based on various statistical metrics using **K-Means clustering**. The result groups similar players together, which can aid in performance analysis and talent segmentation.

## 📁 Dataset

- Filename: `data.csv`
- Encoding: `latin`
- Key columns include player stats, match span, highest scores (`HS`), and career duration.

## 🔧 Steps & Methodology

### 1. **Initial Setup**
- Libraries: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`
- Load data and preview contents.

### 2. **Data Cleaning & Feature Engineering**
- Split and convert `Span` into numeric `start` and `end` years, compute `experience (exp)`.
- Extract `strike` status from `HS` (whether not out).
- Clean `HS` by removing asterisk symbols and converting to integers.
- Drop unnecessary columns (`Span`, `start`, `end`, `Player`).

### 3. **Data Quality Checks**
- Checked for null values and duplicate rows.

### 4. **Outlier Detection and Removal**
- Used **Interquartile Range (IQR)** method on each column to remove statistical outliers.
- Visualized boxplots per feature to inspect distributions.

### 5. **Exploratory Analysis**
- Generated a **heatmap** to inspect correlations among features.

### 6. **Data Normalization**
- Scaled features using `StandardScaler` to standardize value ranges.

### 7. **Clustering with K-Means**
- Applied the **Elbow Method** to determine the optimal number of clusters.
- Trained `KMeans` model (with 4 clusters as chosen).
- Appended cluster labels to the DataFrame.

## 📊 Results
- Cluster assignment successfully completed.
- Cluster counts printed to understand distribution across groups.

## 📌 Requirements

```bash
pip install pandas matplotlib seaborn scikit-learn
```

## 📌 To Run

1. Place `data.csv` in your working directory.
2. Run the Python script or Jupyter notebook containing the code.
