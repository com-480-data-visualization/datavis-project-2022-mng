import pandas as pd
from helpers import ENERGY_REPORTER_HISTORY_CANTON_PATH, \
                    ENERGY_REPORTER_HISTORY_MUNICIPALITY_PATH, \
                    ENERGY_REPORTER_HISTORY_NATIONALITY_PATH, \
                    canton_to_canton_number


def fetch_canton_and_commune_energy():
    df_canton = pd.read_csv(ENERGY_REPORTER_HISTORY_CANTON_PATH)
    df_municipality = pd.read_csv(ENERGY_REPORTER_HISTORY_MUNICIPALITY_PATH)
    df_nationality = pd.read_csv(ENERGY_REPORTER_HISTORY_NATIONALITY_PATH)
    
    df_canton['canton_number'] = df_canton.canton.apply(lambda x: canton_to_canton_number[x])
    df_canton = df_canton.groupby(['canton','canton_number']).agg(list).reset_index()
    
    df_municipality = df_municipality.groupby(['municipality','bfs_nr','canton']).agg(list).reset_index()
    
    df_nationality = df_nationality.groupby('country').agg(list).reset_index()
    
    return df_nationality,df_canton,df_municipality
    
    