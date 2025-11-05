# adding two subclasses: ElectricCar and GasolineCar
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses.
# For example, the initializer of electric cars receives the
# registration number,
# maximum speed and
# battery capacity as its parameters
# It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
# Select speeds for both cars,
# make them drive for three hours and print out the values of their kilometer counters.

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
        print(f"Accelerating by {spd_change} km/h")
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


class ElectricCar(Car):
    def __init__(self, registration_num, max_spd, batt_c):
        super().__init__(registration_num, max_spd)

class GasCar(Car):
    def __init__(self, registration_num, max_spd, fuel):
        super().__init__(registration_num, max_spd)
        self.fuel = fuel

e_car = ElectricCar("ABC-15", 180, 52.5)
g_car = GasCar("ACD-123", 165, 32.3)

car_list = [e_car, g_car]

e_car.accelerate(133)
g_car.accelerate(143)

e_car.drive(3)
g_car.drive(3)

print(f"{"Registration Number":<25}{"Max Speed":<25}{"Current Speed":<25}{"Travel Distance":<25}")
for i in range(len(car_list)):
    print(f"{car_list[i].registration_num:<25}{f"{car_list[i].max_spd} km/h":<25}{f"{car_list[i].current_spd} km/h":<25}{f"{car_list[i].travel_d} km":<25}")
