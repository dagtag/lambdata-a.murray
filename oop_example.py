""" Class module defining car class and subclasses """
class Car:

    def __init__(self, make, model, year, color):
        """ Initializing attributes """
        self.make = make
        self.model = model 
        self.year = year
        self.color = color 
        self.mileage = 0


    def drive(self):
        """ Drives the car """
        print("Driving")

    def set_mileage(self, new_mileage):
        """ Sets mileage to the specified mileage """
        self.mileage = new_mileage 

    def fill_gas(self):
        print("Filling up on gas.")


class ElectricCar(Car):

    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color) # super means parent 
        self.battery = Battery()
    
    def fill_gas(self):
        print("No gas tank.")

class Battery:
    def __init__(self, battery_size = 100):
        self.battery_size = battery_size