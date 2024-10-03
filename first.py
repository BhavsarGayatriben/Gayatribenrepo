

import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return f"{self.registration_number:<10} {self.max_speed:<15} {self.current_speed:<15} {self.travelled_distance:<15}"


cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(registration_number, max_speed))

race_ongoing = True
while race_ongoing:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_ongoing = False

print(f"{'Registration':<10} {'Max Speed (km/h)':<15} {'Current Speed (km/h)':<15} {'Travelled Distance (km)':<15}")
for car in cars:
    print(car)