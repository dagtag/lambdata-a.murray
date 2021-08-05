### Import all functions from helper_functions.py ###
from helper_functions import *
import pytest

### Import pandas and make 2 simple dataframes for testing ###
import pandas as pd
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])

### call Helper class on s1, s2 and call it test_null ###
test_null = Helper(s1, s2)


def test_null_count():
    """ method to test null count, should return 0 nulls """
    assert test_null.null_count(s1) == 0

### Call Helper class on s1, s2 and call it test_comb ###
test_comb = Helper(s1, s2)

def test_combine():
    """ method to test combine method returning two equal dataframes """
    assert test_comb.combine(s1, s2).equals(pd.concat([s1,s2]))

# make patient called patient1 with the following attributes ###
patient1 = Patient(30, 123, 'woman')

def test_patient():
    """ method to test patient method returning patient's age, weight and gender """
    assert patient1.age == 30
    assert patient1.weight == 123
    assert patient1.gender == 'woman'

def test_sleep():
    """ method to test sleep method returning string stating "RX Sleep" """
    assert patient1.sleep() == "RX Sleep"

def test_set_exercise():
    """ method to test setting exercise, should return string stating 
    "Minutes of Exercise: x." """
    assert patient1.set_exercise(30) == "Minutes of Exercise: 30."