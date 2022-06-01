from energy_reporter import fetch_canton_and_commune_energy
from swiss_boundaries import fetch_canton_and_commune_boundaries
from swiss_population import fetch_population_data
from helpers import write_json,WEBSITE_DATA_FILE_PATH
import os
import numpy as np

def merge_canton_datasets(cantons_geo,df_canton,pop_canton):
    cantons_geo_copy = cantons_geo.copy()
    df_canton = df_canton.set_index('canton_number')
    pop_canton = pop_canton.set_index('id')
    
    for i,canton in enumerate(cantons_geo_copy['features']):
        canton_nb = canton['properties']['canton_number']
  
        data_en = df_canton.loc[canton_nb]
        data_pop = pop_canton.loc[canton_nb]
        cantons_geo['features'][i]['properties']['energyreporter_date'] = ' '.join(str(x) for x in data_en['energyreporter_date'])
        cantons_geo['features'][i]['properties']['electric_car_share'] = ' '.join(str(x) for x in data_en['electric_car_share'])
        cantons_geo['features'][i]['properties']['renewable_heating_share'] = ' '.join(str(x) for x in data_en['renewable_heating_share'])
        cantons_geo['features'][i]['properties']['solar_potential_usage'] = ' '.join(str(x) for x in data_en['solar_potential_usage'])
        cantons_geo['features'][i]['properties']['renewable_heating_share_coverage'] = ' '.join(str(x) for x in data_en['renewable_heating_share_coverage'])
        cantons_geo['features'][i]['properties']['abbreviation'] = data_en['canton']
        
        cantons_geo['features'][i]['properties']['population'] = str(data_pop['pop'])
    return cantons_geo

def merge_communes_datasets(communes_geo,df_communes,pop_commune):
    cantons_geo_copy = communes_geo.copy()
    df_communes = df_communes.set_index('bfs_nr')
    pop_commune = pop_commune.set_index('id')
    
    for i,commune in enumerate(cantons_geo_copy['features']):
        commune_nb = commune['properties']['commune_number']
        if commune_nb in df_communes.index:
            data = df_communes.loc[commune_nb]
            communes_geo['features'][i]['properties']['energyreporter_date'] = ' '.join(str(x) for x in data['energyreporter_date'])
            communes_geo['features'][i]['properties']['electric_car_share'] = ' '.join(str(x) for x in data['electric_car_share'])
            communes_geo['features'][i]['properties']['renewable_heating_share'] = ' '.join(str(x) for x in data['renewable_heating_share'])
            communes_geo['features'][i]['properties']['solar_potential_usage'] = ' '.join(str(x) for x in data['solar_potential_usage'])
            communes_geo['features'][i]['properties']['renewable_heating_share_coverage'] = ' '.join(str(x) for x in data['renewable_heating_share_coverage'])
            
        else:
            communes_geo['features'][i]['properties']['energyreporter_date'] = 'null'
            communes_geo['features'][i]['properties']['electric_car_share'] = 'null'
            communes_geo['features'][i]['properties']['renewable_heating_share'] = 'null'
            communes_geo['features'][i]['properties']['solar_potential_usage'] = 'null'
            communes_geo['features'][i]['properties']['renewable_heating_share_coverage'] = 'null'
       
        if commune_nb in pop_commune.index:
            data_pop = pop_commune.loc[commune_nb] 
            communes_geo['features'][i]['properties']['population'] = str(data_pop['pop'])

        else:
            communes_geo['features'][i]['properties']['population'] = 'null'

    return communes_geo

def convert_file_to_topo_json(file_path,new_file_path):
    os.system('geo2topo ' + file_path + ' > ' + new_file_path + ' --quantization 1000')
    os.system('rm '+file_path)

def pipeline_create_data():
    cantons_geo,communes_geo = fetch_canton_and_commune_boundaries()
    df_nationality,df_canton,df_municipality = fetch_canton_and_commune_energy()
    pop_canton,pop_commune = fetch_population_data()
    
    cantons = merge_canton_datasets(cantons_geo,df_canton,pop_canton)
    communes  = merge_communes_datasets(communes_geo,df_municipality,pop_commune)
    

    write_json(cantons,WEBSITE_DATA_FILE_PATH + 'cantons.json')
    write_json(communes,WEBSITE_DATA_FILE_PATH +'communes.json')
    convert_file_to_topo_json(WEBSITE_DATA_FILE_PATH + 'cantons.json', \
                                WEBSITE_DATA_FILE_PATH +'cantons.topo.json')
    convert_file_to_topo_json(WEBSITE_DATA_FILE_PATH + 'communes.json', \
                                WEBSITE_DATA_FILE_PATH +'communes.topo.json')
    
if __name__ == "__main__":
    pipeline_create_data()
    print('created_data')