class Car:
    def __init__(self, registration_num, max_spd, current_spd = 0,
                 travel_d = 0):
        self.registration_num = registration_num
        self.max_spd = max_spd
        self.current_spd = current_spd
        self.travel_d = travel_d

    def properties(self):
        print(f"Registration Number: {self.registration_num}\n"
              f"Max Speed: {self.max_spd} km/h\n"
              f"Current Speed: {self.current_spd} km/h\n"
              f"Travel Distance: {self.travel_d} km")

    def accelerate(self, spd_change):
        print(f"Accelerating by {spd_change} km/h")
        new_spd = spd_change + self.current_spd
        if new_spd < 0:
            self.current_spd = 0
        elif new_spd > self.max_spd:
            self.current_spd = self.max_spd
        else:
            self.current_spd = new_spd

hyundai = Car("ABC-123", 142)


hyundai.properties()
print()
hyundai.accelerate(30)
print()
hyundai.properties()
print()
hyundai.accelerate(70)
print()
hyundai.properties()
print()
hyundai.accelerate(50)
print()
hyundai.properties()
print()
hyundai.accelerate(-200)
print()
hyundai.properties()

