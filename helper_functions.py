""" Import statements """
import pandas as pd
import numpy as np


""" class helper """
class Helper:

    def __init__(self, df1, df2):
        """ Initializing attributes """
        self.df1 = df1
        self.df2 = df2

    def null_count(self, df1, df2):
        """ function providing sum of nulls in a dataframe """
        print(df1.isna().sum())
        print(df2.isna().sum())

    def combine(self, df1, df2):
        """ function concatinating 2 dataframes """
        return pd.concat([df1, df2])


""" Class module defining patient class and subclasses """
class Patient:

    def __init__(self, age, weight, gender):
        """ Initializing attributes """
        self.age = age
        self.weight = weight
        self.gender = gender

    def sleep(self):
        """ Prescribe sleep """
        print("RX Sleep ")

    def set_exercise(self, minutes_of_exercise):
        """ Sets amount of exercise in minutes """
        self.exercise = minutes_of_exercise
        print(f'Minutes of Exercise: ', self.exercise)
