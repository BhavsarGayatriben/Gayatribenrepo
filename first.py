import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

file_path = 'weight-height.csv'
data = pd.read_csv(file_path)

X = data[['Height']]
y = data['Weight']

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
slope = model.coef_[0]
intercept = model.intercept_
print(f"Linear Regression Model: Weight = {slope:.3f} * Height + {intercept:.3f}")
print(f"R^2 Score: {r2:.3f}")
plt.figure(figsize=(8, 6))
plt.scatter(data['Height'], data['Weight'], alpha=0.5, label='Data Points')
plt.plot(data['Height'], y_pred, color='red', linewidth=2, label='Regression Line')
plt.title('Height vs Weight with Regression Line', fontsize=14)
plt.xlabel('Height (inches)', fontsize=12)
plt.ylabel('Weight (pounds)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

