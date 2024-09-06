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