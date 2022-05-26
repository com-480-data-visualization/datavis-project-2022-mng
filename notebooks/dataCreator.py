from energy_reporter import fetch_canton_and_commune_energy
from swiss_boundaries import fetch_canton_and_commune_boundaries
from helpers import write_json,WEBSITE_DATA_FILE_PATH
import os
import numpy as np

def merge_canton_datasets(cantons_geo,df_canton):
    cantons_geo_copy = cantons_geo.copy()
    df_canton = df_canton.set_index('canton_number')
    
    for i,canton in enumerate(cantons_geo_copy['features']):
        canton_nb = canton['properties']['canton_number']
  
        data = df_canton.loc[canton_nb]
        cantons_geo['features'][i]['properties']['energyreporter_date'] = ' '.join(str(x) for x in data['energyreporter_date'])
        cantons_geo['features'][i]['properties']['electric_car_share'] = ' '.join(str(x) for x in data['electric_car_share'])
        cantons_geo['features'][i]['properties']['renewable_heating_share'] = ' '.join(str(x) for x in data['renewable_heating_share'])
        cantons_geo['features'][i]['properties']['solar_potential_usage'] = ' '.join(str(x) for x in data['solar_potential_usage'])
        cantons_geo['features'][i]['properties']['renewable_heating_share_coverage'] = ' '.join(str(x) for x in data['renewable_heating_share_coverage'])
    return cantons_geo

def merge_communes_datasets(communes_geo,df_communes):
    cantons_geo_copy = communes_geo.copy()
    df_communes = df_communes.set_index('bfs_nr')
    
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
            
    return communes_geo

def convert_file_to_topo_json(file_path,new_file_path):
    os.system('geo2topo ' + file_path + ' > ' + new_file_path + ' --quantization 1000')
    os.system('rm '+file_path)

def pipeline_create_data():
    cantons_geo,communes_geo = fetch_canton_and_commune_boundaries()
    df_nationality,df_canton,df_municipality = fetch_canton_and_commune_energy()
    
    cantons = merge_canton_datasets(cantons_geo,df_canton)
    communes  = merge_communes_datasets(communes_geo,df_municipality)
        
    write_json(cantons,WEBSITE_DATA_FILE_PATH + 'cantons.json')
    write_json(communes,WEBSITE_DATA_FILE_PATH +'communes.json')
    convert_file_to_topo_json(WEBSITE_DATA_FILE_PATH + 'cantons.json', \
                                WEBSITE_DATA_FILE_PATH +'cantons.topo.json')
    convert_file_to_topo_json(WEBSITE_DATA_FILE_PATH + 'communes.json', \
                                WEBSITE_DATA_FILE_PATH +'communes.topo.json')
    
if __name__ == "__main__":
    pipeline_create_data()
    print('created_data')