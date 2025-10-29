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

Hyundai = Car("ABC-123", 142)

Hyundai.properties()