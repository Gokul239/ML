🎬 Movie Recommendation System using SVD 
This project implements a collaborative filtering-based movie recommendation system using the Surprise library in Python. It leverages Singular Value Decomposition (SVD) to predict user preferences and provide personalized movie recommendations.

📌 Overview
The notebook walks through the complete process of building a recommendation engine, from data preprocessing to model training and prediction generation. It uses real-world rating data and applies quantile-based filtering to ensure the model is trained on high-quality user-item interactions.

🚀 Features
Load and preprocess user-movie ratings using pandas
Filter out inactive users and unpopular movies using 20th percentile thresholds
Build a recommendation model using Surprise's SVD algorithm
Predict user preferences for unrated movies
Generate top-N recommendations for a given user
Visualize user activity and rating distributions
🧠 Key Components
Reader: Defines the format and scale of the input rating data.
Dataset: Converts pandas DataFrame into a Surprise-compatible dataset.
SVD: Performs matrix factorization for collaborative filtering.
top_recommendation(): Custom function to generate recommendations using predicted ratings.
📊 Data Handling
The system filters users and movies based on activity levels using quantile thresholds.
Predictions are generated using Surprise’s .predict() method for each user-item pair.
🔧 Requirements
Python 3.x
pandas
seaborn
matplotlib
scikit-surprise (pip install scikit-surprise)
