import json

DATA_FOLDER_PATH = '../data/' #change path if needed
BORDERS_PATH = DATA_FOLDER_PATH + 'swissboundaries3d_2022-01_2056_5728.shp/SHAPEFILE_LV95_LN02/'

ENERGY_REPORTER_PATH = DATA_FOLDER_PATH + 'energyreporter_historized/'

COMUNES_PATH = BORDERS_PATH  + "swissBOUNDARIES3D_1_3_TLM_HOHEITSGEBIET.shp"
CANTON_PATH = BORDERS_PATH + "swissBOUNDARIES3D_1_3_TLM_KANTONSGEBIET.shp"
ENERGY_REPORTER_HISTORY_PATH = DATA_FOLDER_PATH + 'energyreporter_historized/'
ENERGY_REPORTER_LATEST_PATH = DATA_FOLDER_PATH + 'energyreporter_latest/'

#CSV FILE HISTORIZED PATHS
ENERGY_REPORTER_HISTORY_CANTON_PATH = ENERGY_REPORTER_HISTORY_PATH + 'energyreporter_canton_historized.csv'
ENERGY_REPORTER_HISTORY_MUNICIPALITY_PATH = ENERGY_REPORTER_HISTORY_PATH + 'energyreporter_municipality_historized.csv'
ENERGY_REPORTER_HISTORY_NATIONALITY_PATH = ENERGY_REPORTER_HISTORY_PATH + 'energyreporter_national_historized.csv'

def write_json(dictionary, filepath):
    with open(filepath, "w") as final:
        json.dump(dictionary, final)
        
        