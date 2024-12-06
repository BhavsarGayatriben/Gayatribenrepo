# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

# Load the dataset
file_path ='C:/Users/Gayatri Bhavsar/PycharmProjects/first.py/suv.csv' # Replace with your file path
data = pd.read_csv(file_path)

# Select features and target variable
X = data[['Age', 'EstimatedSalary']]
y = data['Purchased']

# Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using standard scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Function to train Decision Tree Classifier and evaluate performance
def evaluate_decision_tree(criterion, X_train, X_test, y_train, y_test):
    dt = DecisionTreeClassifier(criterion=criterion, random_state=42)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)
    return cm, cr

# Evaluate with entropy criterion
print("Decision Tree with Entropy Criterion:")
cm_entropy, cr_entropy = evaluate_decision_tree('entropy', X_train_scaled, X_test_scaled, y_train, y_test)
print("Confusion Matrix:\n", cm_entropy)
print("Classification Report:\n", cr_entropy)

# Evaluate with gini criterion
print("Decision Tree with Gini Criterion:")
cm_gini, cr_gini = evaluate_decision_tree('gini', X_train_scaled, X_test_scaled, y_train, y_test)
print("Confusion Matrix:\n", cm_gini)
print("Classification Report:\n",cr_gini)