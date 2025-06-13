# 🧠 Hierarchical Clustering for Customer Segmentation

## 📌 Objective

This project applies **Hierarchical Clustering** to group customers based on their **annual income**, **spending score**, **age**, and **region**. It aims to uncover meaningful customer segments that can guide business strategies like targeted marketing or personalized recommendations.

---

## 🛠️ Tools & Libraries Used

- **Pandas** – Data manipulation
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Preprocessing (StandardScaler, LabelEncoder)
- **Scipy** – Hierarchical clustering (`linkage`, `fcluster`, `dendrogram`)
- **Plotly** – Interactive 3D visualization

---

## 📊 Dataset Description

The dataset includes the following columns:

- `CustomerID` – Unique customer identifier (removed before clustering)
- `Annual_Income` – Yearly income of the customer
- `Spending_Score` – Score assigned based on customer spending behavior
- `Age` – Age of the customer
- `Region` – Categorical variable representing customer's region

---

## 🧹 Preprocessing Steps

1. **Dropped `CustomerID`** as it has no clustering value.
2. **Checked for null and duplicate values**.
3. **Normalized** quantitative features using `StandardScaler`.
4. **One-hot encoded** the categorical `Region` column.
5. Combined all features into a final DataFrame for clustering.

---

## 📈 Hierarchical Clustering

- Used `scipy.cluster.hierarchy.linkage` with the **Ward method** to minimize intra-cluster variance.
- Plotted a **dendrogram** to visualize hierarchical merges and decide the number of clusters.
- Applied `fcluster` with `criterion='maxclust'` to form **exactly 4 clusters**.

---

## 📊 Visualizations

- **Pairplot** to visualize cluster separation in 2D across numerical features.
- **3D Scatter Plot** using Plotly for interactive cluster analysis based on `Annual_Income`, `Spending_Score`, and `Age`.

---

## 📌 Output

The final dataset includes a new column `cluster` indicating the predicted group for each customer. These segments can now be further analyzed or used in marketing strategies.

---
