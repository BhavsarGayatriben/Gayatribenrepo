import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

# Step 0: Reading the uploaded CSV file into a Pandas DataFrame
file_path = 'C:/Users/Gayatri Bhavsar/PycharmProjects/first.py/data_banknote_authentication.csv'
data = pd.read_csv(file_path)

# Step 1: Define target variable y and feature variables X
X = data.drop(columns=['class'])
y = data['class']

# Step 2: Split data into training and testing sets with an 80/20 split and random_state=20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

# Step 3: Train a support vector classifier with a linear kernel
svc_linear = SVC(kernel='linear', random_state=20)
svc_linear.fit(X_train, y_train)

# Step 4: Predict on the testing data and compute the confusion matrix and classification report
y_pred_linear = svc_linear.predict(X_test)
conf_matrix_linear = confusion_matrix(y_test, y_pred_linear)
class_report_linear = classification_report(y_test, y_pred_linear)

# Step 5: Train a support vector classifier with an RBF kernel
svc_rbf = SVC(kernel='rbf', random_state=20)
svc_rbf.fit(X_train, y_train)

# Step 6: Predict on the testing data and compute the confusion matrix and classification report
y_pred_rbf = svc_rbf.predict(X_test)
conf_matrix_rbf = confusion_matrix(y_test, y_pred_rbf)
class_report_rbf = classification_report(y_test, y_pred_rbf)

# Print results
print("Linear Kernel SVM:")
print("Confusion Matrix:\n", conf_matrix_linear)
print("Classification Report:\n", class_report_linear)

print("\nRBF Kernel SVM:")
print("Confusion Matrix:\n", conf_matrix_rbf)
print("Classification Report:\n", class_report_rbf)