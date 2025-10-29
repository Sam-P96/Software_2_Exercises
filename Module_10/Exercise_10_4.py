import random

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
              f"Travel Distance: {self.travel_d} km\n")

    def accelerate(self, spd_change):
        # print(f"Accelerating by {spd_change} km/h")
        new_spd = spd_change + self.current_spd
        if new_spd < 0:
            self.current_spd = 0
        elif new_spd > self.max_spd:
            self.current_spd = self.max_spd
        else:
            self.current_spd = new_spd

    def drive(self, time):
        distance = time * self.current_spd
        self.travel_d += distance
        if time > 1:
            print(f"Driving for {time} hours at {self.current_spd}.")
        else:
            print(f"Driving for {time} hour at {self.current_spd}.")

class Race:
    def __init__(self, name, km, c_list):
        self.name = name
        self.race_length = km
        self.c_list = c_list

    def hour_passes(self):
        for i in range(len(self.c_list)):
            self.c_list[i].accelerate(random.randint(-10, 15))
            self.c_list[i].drive(1)
    def print_status(self):
        for car in self.c_list:
            car.properties()

    def race_finished(self):
        for car in self.c_list:
            if car.travel_d > self.race_length:
                print("Race Ended")
                return True
            else:
                return False
        return None

car_list = []
for i in range(10): # creation of the cars in the race from the previous program
    car_list.append(Car(f"ABC-{i + 1}", random.randint(100,200)))

dd_race = Race("Grand Demolition Derby", 8000, car_list)
dd_race.print_status()

while not dd_race.race_finished(): # I originally had while dd_race.race_finished != True, or something like that
    for i in range(10): # for every 10 hour
        dd_race.hour_passes()
    print()
    dd_race.print_status()








