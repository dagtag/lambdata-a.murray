### Making a basic function to test with pytest ###

def inc(x):
    """ Increments number by one """
    return x + 1

class Car:
    """ Class module defining car class and subclasses """

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
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            print("Can't take away miles")

    def fill_gas(self):
        """ Filling up gas tank """
        print("Filling up on gas.")