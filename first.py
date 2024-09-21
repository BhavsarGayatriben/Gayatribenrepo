import random
num_dice = int(input("How many dice would you like to roll? "))

total_sum = 0
for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print(f"The sum of the rolls is: {total_sum}")

numbers = []


while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == '':
        break
    else:
        try:
            numbers.append(int(user_input))
        except ValueError:
            print("Please enter a valid number.")


numbers.sort(reverse=True)
top_5 = numbers[:5]
print("The top 5 greatest numbers are:", top_5)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


number = int(input("Enter an integer: "))


if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")