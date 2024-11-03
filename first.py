import numpy as np

# Define matrix A
A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

# Calculate the inverse of A
A_inv = np.linalg.inv(A)

# Calculate A * A_inv and A_inv * A
identity_1 = np.dot(A, A_inv)
identity_2 = np.dot(A_inv, A)

# Print results
print("Matrix A:")
print(A)

print("\nInverse of Matrix A (A^-1):")
print(A_inv)

print("\nA * A^-1 (Should approximate identity matrix):")
print(identity_1)

print("\nA^-1 * A (Should approximate identity matrix):")
print(identity_2)

# Optionally, check if the results are close to the identity matrix
print("\nAre A * A^-1 and A^-1 * A close to the identity matrix?")
print(np.allclose(identity_1, np.eye(3)))  # True if close to identity matrix
print(np.allclose(identity_2, np.eye(3)))  # True if close to identity matrix