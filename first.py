# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# Load the dataset
file_path = 'C:/Users/Gayatri Bhavsar/PycharmProjects/first.py/weight-height.csv'
data = pd.read_csv(file_path)

# Convert height to centimeters and weight to kilograms
data['Height'] = data['Height'] * 2.54  # inches to cm
data['Weight'] = data['Weight'] * 0.453592  # pounds to kg

# Define feature and target variables
X = data[['Height']]  # Feature variable (in cm)
y = data['Weight']    # Target variable (in kg)

# Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
# Normalization (Min-Max scaling)
min_max_scaler = MinMaxScaler()
X_train_norm = min_max_scaler.fit_transform(X_train)
X_test_norm = min_max_scaler.transform(X_test)

# Standardization (Z-score scaling)
standard_scaler = StandardScaler()
X_train_std = standard_scaler.fit_transform(X_train)
X_test_std = standard_scaler.transform(X_test)

# Function to fit KNN and compute R^2 score
def knn_r2_score(X_train, X_test, y_train, y_test, k=5):
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return r2_score(y_test, y_pred)

# Evaluate KNN regression with different scalings
r2_unscaled = knn_r2_score(X_train, X_test, y_train, y_test)
r2_normalized = knn_r2_score(X_train_norm, X_test_norm, y_train, y_test)
r2_standardized = knn_r2_score(X_train_std, X_test_std, y_train, y_test)

# Print R^2 values for comparison
print(f"R^2 without scaling: {r2_unscaled}")
print(f"R^2 with normalization: {r2_normalized}")
print(f"R^2 with standardization: {r2_standardized}")
