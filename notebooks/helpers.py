import json

DATA_FOLDER_PATH = '../data/' #change path if needed
BORDERS_PATH = DATA_FOLDER_PATH + 'swissboundaries3d_2022-01_2056_5728.shp/SHAPEFILE_LV95_LN02/'

ENERGY_REPORTER_PATH = DATA_FOLDER_PATH + 'energyreporter_historized/'

COMUNES_PATH = BORDERS_PATH  + "swissBOUNDARIES3D_1_3_TLM_HOHEITSGEBIET.shp"
CANTON_PATH = BORDERS_PATH + "swissBOUNDARIES3D_1_3_TLM_KANTONSGEBIET.shp"
ENERGY_REPORTER_HISTORY_PATH = DATA_FOLDER_PATH + 'energyreporter_historized/'
ENERGY_REPORTER_LATEST_PATH = DATA_FOLDER_PATH + 'energyreporter_latest/'

#population data
POPULATION_PATH = DATA_FOLDER_PATH + 'px-x-0102020000_201_20220406-142814.xlsx'

#CSV FILE HISTORIZED PATHS
ENERGY_REPORTER_HISTORY_CANTON_PATH = ENERGY_REPORTER_HISTORY_PATH + 'energyreporter_canton_historized.csv'
ENERGY_REPORTER_HISTORY_MUNICIPALITY_PATH = ENERGY_REPORTER_HISTORY_PATH + 'energyreporter_municipality_historized.csv'
ENERGY_REPORTER_HISTORY_NATIONALITY_PATH = ENERGY_REPORTER_HISTORY_PATH + 'energyreporter_national_historized.csv'

WEBSITE_DATA_FILE_PATH = '../src/data/'

canton_to_canton_number = {'AG': 19, \
                           'AI': 16, \
                           'AR': 15, \
                           'BE': 2, \
                           'BL': 13, \
                           'BS': 12, \
                           'FR': 10, \
                           'GE': 25, \
                           'GL': 8, \
                           'GR': 18, \
                           'JU': 26, \
                           'LU': 3, \
                           'NE': 24, \
                           'NW': 7, \
                           'OW': 6, \
                           'SG': 17, \
                           'SH': 14, \
                           'SO': 11, \
                           'SZ': 5, \
                           'TG': 20,  \
                           'TI': 21, \
                           'UR': 4, \
                           'VD': 22, \
                           'VS': 23, \
                           'ZG': 9, \
                           'ZH': 1}

canton_pop_to_canton_number = {'Aargau': 19, \
                           'Appenzell Innerrhoden': 16, \
                           'Appenzell Ausserrhoden': 15, \
                           'Bern / Berne': 2, \
                           'Basel-Landschaft': 13, \
                           'Basel-Stadt': 12, \
                           'Fribourg / Freiburg': 10, \
                           'Genève': 25, \
                           'Glarus': 8, \
                           'Graubünden / Grigioni / Grischun': 18, \
                           'Jura': 26, \
                           'Luzern': 3, \
                           'Neuchâtel': 24, \
                           'Nidwalden': 7, \
                           'Obwalden': 6, \
                           'St. Gallen': 17, \
                           'Schaffhausen': 14, \
                           'Solothurn': 11, \
                           'Schwyz': 5, \
                           'Thurgau': 20,  \
                           'Ticino': 21, \
                           'Uri': 4, \
                           'Vaud': 22, \
                           'Valais / Wallis': 23, \
                           'Zug': 9, \
                           'Zürich': 1}

def write_json(dictionary, filepath):
    with open(filepath, "w") as final:
        json.dump(dictionary, final)
        
        