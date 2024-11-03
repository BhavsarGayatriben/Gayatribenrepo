import csv
import numpy as np
import matplotlib.pyplot as plt

# Path to the CSV file (replace with the correct path to your file)
file_path = 'path/to/weight-height.csv'  # Replace this with your actual file path

# Read data from the CSV file into a list, then convert to a numpy array
data = []

try:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if there is one
        for row in reader:
            # Append each row as a tuple (length, weight) converted to float
            data.append((float(row[0]), float(row[1])))  # Assuming length is in column 1 and weight in column 2

    # Convert the list to a numpy array
    data = np.array(data)

    # Separate columns for length and weight
    length_in_inches = data[:, 0]  # First column for length
    weight_in_pounds = data[:, 1]  # Second column for weight

    # Convert lengths to centimeters and weights to kilograms
    length_cm = length_in_inches * 2.54
    weight_kg = weight_in_pounds * 0.453592

    # Calculate the means of lengths and weights
    mean_length = np.mean(length_cm)
    mean_weight = np.mean(weight_kg)

    print("Mean Length (cm):", mean_length)
    print("Mean Weight (kg):", mean_weight)

    # Plot histogram of lengths in centimeters
    plt.hist(length_cm, bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogram of Lengths in cm')
    plt.xlabel('Length (cm)')
    plt.ylabel('Frequency')
    plt.show()

except FileNotFoundError:
    print(f"The file at path '{file_path}' was not found. Please check the file path and try again.")