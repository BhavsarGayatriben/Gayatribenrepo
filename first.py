# Function to calculate the sum of integers in a list
def sum_of_list(numbers):
    return sum(numbers)

# Main program: create a list and call the sum function
def main():
    numbers = [1, 2, 3, 4, 5]
    total = sum_of_list(numbers)
    print(f"The sum of the list {numbers} is {total}")

main()