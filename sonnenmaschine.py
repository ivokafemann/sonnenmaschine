import time
import pandas as pd
import numpy as np

A_pv = 20
n_pv = 0.2
gamma = 1

def load_data():
    """
    Loads weather data into a data frame.

    Returns:
        df - Pandas DataFrame containing global horizontal irradiance (ghi) for evergy hour of the year.
    """

    # load data file into a dataframe
    df = pd.read_csv('input_potsdam.csv')

    return df
    print(df.head())
