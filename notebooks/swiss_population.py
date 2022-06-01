import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import unidecode
from helpers import POPULATION_PATH,canton_pop_to_canton_number


def assign_region_type(region):
    if region[0] == '-':
        return 'canton'
    elif region[:2] == '>>':
        return 'district'
    elif region[:6] == '......':
        return 'commune'
    else:
        return 'country'
    
    
def clean_region(region):
    words = region.split()
    if len(words) > 1:
        return ' '.join(words[1:])
    else:
        return words[0]

def fetch_population_data():
    
    pop_df = pd.read_excel(POPULATION_PATH,header=2)
    
    pop_df = pop_df.rename(columns ={'Unnamed: 4': 'population_type', 'Unnamed: 2': 'region', 'Unnamed: 1': 'year'}) \
                .drop(columns = ['Unnamed: 3','Unnamed: 0']) \
                .fillna(method="ffill")
    pop_df = pop_df[pop_df.region != 'Unknown']
    
    pop_df['region_type'] = pop_df.region.apply(assign_region_type)
    pop_df['bfs_nb'] = pop_df.region.apply(lambda x: re.findall(r'^\D*(\d+)', x)[0] if x[:6] == '......' else np.nan)

    pop_df['region'] = pop_df.region.apply(clean_region)
    pop_df['Population on 1 January'] = pop_df['Population on 1 January'].apply(int)
    pop_df['year'] = pop_df['year'].apply(int)
    
    pop_commune = pop_df[(pop_df.region_type == 'commune') & (pop_df.population_type == 'Sex - total')]
    pop_canton = pop_df[(pop_df.region_type == 'canton') & (pop_df.population_type == 'Sex - total')]
    
    pop_canton = pop_canton.sort_values(by = ['year']).drop_duplicates(subset = ['region'], keep = 'last')
    pop_commune = pop_commune.sort_values(by = ['year']).drop_duplicates(subset = ['region'], keep = 'last')
    
    pop_commune = pop_commune[['region','Population on 1 January','bfs_nb']] \
                            .rename(columns = {'Population on 1 January': 'pop', 'bfs_nb': 'id'})
                            
    pop_canton = pop_canton[['region','Population on 1 January','bfs_nb']] \
                            .rename(columns = {'Population on 1 January': 'pop', 'bfs_nb': 'id'})
                            
    pop_canton['id'] = pop_canton.region.apply(lambda x: canton_pop_to_canton_number[x])
    pop_commune['id'] = pop_commune['id'].apply(lambda x: int(x))
    
    return pop_canton,pop_commune