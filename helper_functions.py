import pandas as pd
import numpy as np

def null_count(df):
    return df.isna().sum()

def combine(df_left, df_right):
    return pd.concat([df_left, df_right])
