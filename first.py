import random

def calculate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside_circle += 1

    pi_approx = 4 * inside_circle / num_points
    return pi_approx

num_points = int(input("Enter the number of random points to generate: "))
approx_pi = calculate_pi(num_points)
print(f"Approximation of pi: {approx_pi}")