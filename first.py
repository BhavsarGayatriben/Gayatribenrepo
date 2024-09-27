def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = remove_odd_numbers(numbers)
    print(f"Original list: {numbers}")
    print(f"List after removing odd numbers: {even_numbers}")

main()