import pandas as pd
from helpers import *



def load_energy_reporter_data():
    df_canton = pd.read_csv(ENERGY_REPORTER_HISTORY_CANTON_PATH)
    df_municipality = pd.read_csv(ENERGY_REPORTER_HISTORY_MUNICIPALITY_PATH)
    df_nationality = pd.read_csv(ENERGY_REPORTER_HISTORY_NATIONALITY_PATH)
    return df_canton,df_municipality,df_nationality
