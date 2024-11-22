#Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load Diabetes Dataset
data = load_diabetes()
X = data.data
y = data.target

# Convert to DataFrame for clarity
columns = data.feature_names
df = pd.DataFrame(X, columns=columns)
df['target'] = y

# Feature Exploration
print("Dataset Head:\n", df.head())
print("\nFeature Correlation with Target:")
print(df.corr()['target'].sort_values(ascending=False))

"""
Explanation
We start by analyzing the correlation of each variable with the target. Higher correlation may suggest that a feature is
a good candidate for predicting diabetes progression.
"""

# Split the data for initial analysis with just bmi and s5
X_baseline = df[['bmi', 's5']]
X_train, X_test, y_train, y_test = train_test_split(X_baseline, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Baseline model using only 'bmi' and 's5'
model_baseline = LinearRegression()
model_baseline.fit(X_train_scaled, y_train)

# Predictions and Metrics for baseline
y_pred_baseline = model_baseline.predict(X_test_scaled)
mse_baseline = mean_squared_error(y_test, y_pred_baseline)
r2_baseline = r2_score(y_test, y_pred_baseline)

print("\nBaseline Model Performance (using only bmi and s5):")
print(f"Mean Squared Error: {mse_baseline}")
print(f"R2 Score: {r2_baseline}")

# Add additional feature: Let's choose 'bp' (Blood Pressure) based on correlation analysis
X_expanded = df[['bmi', 's5', 'bp']]
X_train_exp, X_test_exp, y_train, y_test = train_test_split(X_expanded, y, test_size=0.2, random_state=42)

# Standardize the features
X_train_exp_scaled = scaler.fit_transform(X_train_exp)
X_test_exp_scaled = scaler.transform(X_test_exp)

# Expanded model with an additional variable
model_expanded = LinearRegression()
model_expanded.fit(X_train_exp_scaled, y_train)

# Predictions and Metrics for expanded model
y_pred_expanded = model_expanded.predict(X_test_exp_scaled)
mse_expanded = mean_squared_error(y_test, y_pred_expanded)
r2_expanded = r2_score(y_test, y_pred_expanded)

print("\nExpanded Model Performance (adding 'bp'):")
print(f"Mean Squared Error: {mse_expanded}")
print(f"R2 Score: {r2_expanded}")

"""
Findings for Step b:
Adding the 'bp' (Blood Pressure) variable increases the R2 score and reduces the MSE, indicating that
'bp' is a useful predictor when combined with 'bmi' and 's5'.
"""

# Additional Investigation: Adding all features to see if it further improves
X_all = df.drop('target', axis=1)
X_train_all, X_test_all, y_train, y_test = train_test_split(X_all, y, test_size=0.2, random_state=42)

# Standardize all features
X_train_all_scaled = scaler.fit_transform(X_train_all)
X_test_all_scaled = scaler.transform(X_test_all)

# Model using all features
model_all = LinearRegression()
model_all.fit(X_train_all_scaled, y_train)

# Predictions and Metrics for the model with all features
y_pred_all = model_all.predict(X_test_all_scaled)
mse_all = mean_squared_error(y_test, y_pred_all)
r2_all = r2_score(y_test, y_pred_all)

print("\nFull Model Performance (using all features):")
print(f"Mean Squared Error: {mse_all}")
print(f"R2 Score: {r2_all}")
