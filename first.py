import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('bank.csv', delimiter=';')
print("Dataset Head:\n", data.head())
print("\nColumns and Types:\n", data.info())

df2 = data[['y', 'job', 'marital', 'default', 'housing', 'poutcome']]
print("\nSelected DataFrame:\n", df2.head())

df3 = pd.get_dummies(df2, columns=['job', 'marital', 'default', 'housing', 'poutcome'], drop_first=True)
print("\nDataFrame with Dummy Variables:\n", df3.head())

df3['y'] = (df3['y'] == 'yes').astype(int)

correlation_matrix = df3.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()