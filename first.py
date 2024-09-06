name = input("What is your name? ")
print(f"Hello, {name}!")
import math


radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The area of the circle with radius {radius} is {area:.2f}")

length = float(input("Enter the length of the rectangle: "))

width = float(input("Enter the width of the rectangle: "))
area = length * width

perimeter = 2 * (length + width)

print(f"The area of the rectangle is {area:.2f}")
print(f"The perimeter of the rectangle is {perimeter:.2f}")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))



total_sum = num1 + num2 + num3


product = num1 * num2 * num3

average = total_sum / 3

print(f"Sum: {total_sum}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
lots_in_pound = 32
pounds_in_talent = 20
grams_in_lot = 13.3


talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))


total_lots = (talents * pounds_in_talent * lots_in_pound) + (pounds * lots_in_pound) + lots

total_grams = total_lots * grams_in_lot

import random
code_3_digits = [random.randint(0, 9) for _ in range(3)]
code_4_digits = [random.randint(1, 6) for _ in range(4)]
code_3_digits_str = ''.join(map(str, code_3_digits))
code_4_digits_str = ''.join(map(str, code_4_digits))

size_limit = 42


zander_length = float(input("Enter the length of the zander in cm: "))
if zander_length >= size_limit:
    print("The zander meets the size limit. You can keep it.")
else:
    difference = size_limit - zander_length
    print(f"Release the fish back into the lake. It is {difference:.2f} cm below the size limit.")

    cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()


    if cabin_class == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("A: above the car deck, equipped with a window.")

    elif cabin_class == "B":
        print("B: windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")

        gender = input("Enter biological gender (male/female): ").strip().lower()
        hemoglobin = float(input("Enter hemoglobin value (g/l): "))


        if gender == "female":
            if hemoglobin < 117:
                print("Hemoglobin value is low.")
            elif 117 <= hemoglobin <= 155:
                print("Hemoglobin value is normal.")
            else:
                print("Hemoglobin value is high.")
        elif gender == "male":
            if hemoglobin < 134:
                print("Hemoglobin value is low.")
            elif 134 <= hemoglobin <= 167:
                print("Hemoglobin value is normal.")
            else:
                print("Hemoglobin value is high.")
        else:
            print("Invalid gender. Please enter 'male' or 'female'.")

            year = int(input("Enter a year: "))


            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")