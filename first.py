import random
num_dice = int(input("How many dice would you like to roll? "))

total_sum = 0
for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print(f"The sum of the rolls is: {total_sum}")