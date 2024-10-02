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
        return f"Registration Number: {self.registration_number}, Max Speed: {self.max_speed} km/h, Current Speed: {self.current_speed} km/h, Travelled Distance: {self.travelled_distance} km"

# Main program
car = Car("ABC-123", 142)
car.accelerate(60)  # Speed up to 60 km/h
car.drive(1.5)      # Drive for 1.5 hours
print(f"After driving: {car}")