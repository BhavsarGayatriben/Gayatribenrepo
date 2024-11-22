import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

file_path = 'weight-height.csv'
data = pd.read_csv(file_path)
X = data[['Height']]
y = data['Weight']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)
print(f"Root Mean Square Error (RMSE): {rmse:.3f}")
print(f"R^2 Score: {r2:.3f}")

