### HELPER FUNCTIONS TURNED INTO CLASSES FOR OOP ###

import pandas as pd
import numpy as np


class Helper:
    """ Class Helper with useful modules null_counts and combine """


    def __init__(self, df1, df2):
        """ Initializing dataframe attributes """
        self.df1 = df1
        self.df2 = df2

    def null_count(self, df):
        """ Module returning sum of nulls in a dataframe """
        return df.isna().sum()

    def combine(self, df1, df2):
        """ Module returning two concatinated dataframes """
        return pd.concat([df1, df2])


class Patient:
    """ Class module defining patient class and subclasses """


    def __init__(self, age, weight, gender):
        """ Initializing patient attributes """
        self.age = age
        self.weight = weight
        self.gender = gender

    def sleep(self):
        """ Prescribes sleep, returns "RX Sleep" """
        return "RX Sleep"

    def set_exercise(self, minutes_of_exercise):
        """ Sets amount of exercise in minutes and returns "Minutes of Exercise: x " """
        self.exercise = minutes_of_exercise
        return f"Minutes of Exercise: {self.exercise}."