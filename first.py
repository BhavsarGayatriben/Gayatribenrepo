
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

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Max Speed: {self.max_speed} km/h, Current Speed: {self.current_speed} km/h, Travelled Distance: {self.travelled_distance} km"

# Main program
car = Car("ABC-123", 142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current Speed after accelerating: {car.current_speed} km/h")
car.accelerate(-200)
print(f"Final Speed after emergency brake: {car.current_speed} km/h")

