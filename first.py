import pandas as pd
import matplotlib.pyplot as plt

file_path = 'weight-height.csv'
data = pd.read_csv(file_path)

plt.figure(figsize=(8, 6))
plt.scatter(data['Height'], data['Weight'], alpha=0.5, color='red')
plt.title('Scatter Plot of Height vs Weight', fontsize=14)
plt.xlabel('Height (inches)', fontsize=12)
plt.ylabel('Weight (pounds)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

