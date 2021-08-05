### TEST FILE USING ASSERT STATEMENTS AND PYTEST FOR UNIT TESTING ###

### import statements 
import pytest
from sample import inc

def test_inc_pint():
    """ method to test inc function with positive ints """
    assert inc(10) == 11
    assert inc(2) == 3

def test_inc_zero():
    """ method to test inc function with zero """
    assert inc(0) == 1

def test_inc_nn():
    """ method to test inc function with negative numbers """
    assert inc(-1) == 0

def test_inc_flt():
    """ method to test inc function with floats """
    assert inc(1.5) == 2.5

### testing Car class modules 
from sample import Car

### use car class to make an instance of my_car 
my_car = Car("Toyota", "Tundra", 2021, 'Silver')

def test_make():
    """ method to test make of car """
    assert my_car.make == "Toyota"

def test_model():
    """ method to test model of car """
    assert my_car.model == "Tundra"

def test_year():
    """ method to test year of car """
    assert my_car.year == 2021

def test_color():
    """ method to test color of car """
    assert my_car.color == "Silver"


# to run in terminal type: pytest test_sample.py --verbose
# to run test file, HAVE TO HAVE "test_" in title of file AND in def function 