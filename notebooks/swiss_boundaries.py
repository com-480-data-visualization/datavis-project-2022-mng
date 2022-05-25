import shapefile
import unidecode
import matplotlib.pyplot as plt
import json
from helpers import COMUNES_PATH,CANTON_PATH


def seperate_by_borders(coordinates):
    """some records contain the coordinates of more than one border. Therefore we must seperate these in seperate lists"""
    #input: - coordinates: which is a list of coordinates
    #output: - ls_of_borders which is a list of list. Each list is a border (either of a commune or a canton depending what we called)
    ls_of_borders = []
    border_start = None
    tmp = []
    #iterate coordinates
    for i,(coord) in enumerate(coordinates):
        if border_start is None:
            #if therer is no starting coordinate define one
            border_start = coord
            tmp = []
            #append to tmp which is a list that keeps all the coordinates of a border
            tmp.append((int(round(coord[0],0)),int(round(coord[1],0))))
        
        #if we find a coordinate that is the same as border start, then we have a closed loop of coordinates.
        # which means that we have a full border
        elif coord == border_start or  i == len(coordinates)-1:
            tmp.append((int(round(coord[0],0)),int(round(coord[1],0))))
            #append border to final solution
            ls_of_borders.append(tmp)
            border_start = None
            
        #if we don't find a coordinate that is the same as border start, then we don't have a closed loop of coordinates. 
        else:
            #keep on appending coordinates to tmp
            tmp.append((int(round(coord[0],0)),int(round(coord[1],0))))
            
    return ls_of_borders
     

def order_coordinates(area):
    """Function that identifies all of the borders of a canton or a commune. In fact, there may be more than one border
        (e.g. look on google maps the for ticino. There is more than one border. One is the outer border of ticino. But
        there is also a border between ticino and campione d'italia) """

    #list containing all borders
    all_borders = []
    ls_of_borders = []
    for record in area:
        #get coordinates of record
        coordinates = record.shape.points
        #first border
        ls_of_borders = seperate_by_borders(coordinates)

        for border in ls_of_borders:
            all_borders.append(border)

    
    return all_borders





def fetch_cantons_dictionary_geojson(canton_sf):
    """Accesses data from shapefile and returns all swiss cantons in dictionary"""
    #input: sf: data loaded from shapefile
    #output: dictionary with 3 keys: name (name of canton),
    #                                border (coordinates of the border),
    #                                canton_number (id of canton)
    canton_info = dict()
    canton_final_dict = dict()
    canton_final_dict['type'] = 'FeatureCollection'
    canton_final_dict['features'] = []
    #iterate records of shapefile
    for i in range(len(canton_sf)):
        #KANTONSNUM is the id of the canton. and rec.record['OBJEKTART'] == 'Kanton'
        #checks if the record is about a kanton
        
        #checks if one of the borders of the canton is already in the dictionary, if yes append record
        rec = canton_sf.shapeRecord(i)
        if rec.record['KANTONSNUM'] in canton_info and rec.record['OBJEKTART'] == 'Kanton':
            canton_info[rec.record['KANTONSNUM']].append(rec)
        #if one of the borders of the canton is not already in the dictionary, add record in a list
        elif rec.record['KANTONSNUM'] not in canton_info and rec.record['OBJEKTART'] == 'Kanton':
            canton_info[rec.record['KANTONSNUM']] = [rec]
   
    for canton in canton_info:
        #puts all borders of a canton into one single list of coodinates
        canton_border = order_coordinates(canton_info[canton].copy())
        #fetch the name of the canton
        canton_name = canton_info[canton][0].record['NAME']
        #remove accents
        canton_name = unidecode.unidecode(canton_name)
        #fetch id of canton
        canton_number = canton_info[canton][0].record['KANTONSNUM']
        #add info
       
       
        canton_properties = {'name': canton_name,'canton_number': canton_number}
        canton_geometry = {'type': 'MultiPolygon', 'coordinates': [list(map(lambda x: list(x), canton_border))]}
        canton_dict = {'type': 'Feature','properties': canton_properties , 'geometry': canton_geometry}
        canton_final_dict['features'].append(canton_dict)
    return canton_final_dict

def fetch_communes_dictionary_geojson(sf):
    """Accesses data from shapefile and returns all swiss communes in dictionary"""
    #input: sf: data loaded from shapefile
    #output: dictionary with 3 keys: name (name of commune),
    #                                border (coordinates of the border),
    #                                canton_number (id of canton that the commune is in)
    communes = dict()
    communes_final_dict = dict()
    communes_final_dict['type'] = 'FeatureCollection'
    communes_final_dict['features'] = []
    #iterate shapefile
    for i in range(len(sf)):
        #acces record 
        rec = sf.shapeRecord(i)
        
        #BFS_NUMMER is the id of the commune. and rec.record['OBJEKTART'] == 'Gemeindegebiet'
        #checks if the record is about a commune
        
        #checks if one of the borders of the commune is already in the dictionary, if yes append record
        if rec.record['BFS_NUMMER'] in communes and rec.record['OBJEKTART'] == 'Gemeindegebiet':
            communes[rec.record['BFS_NUMMER']].append(rec)
        #if one of the borders of the commune is not already in the dictionary, add record in a list
        elif rec.record['BFS_NUMMER'] not in communes and rec.record['OBJEKTART'] == 'Gemeindegebiet':
            communes[rec.record['BFS_NUMMER']] = [rec]
    
    
    for commune in communes:
        #puts all borders of a commune into one single list of coodinates
        commune_border = order_coordinates(communes[commune].copy())
        #fetch the name of the commune
        commune_name = communes[commune][0].record['NAME']
        #remove accents
        commune_name = unidecode.unidecode(commune_name)
        #fetch id of canton that the commune is in
        canton_number = communes[commune][0].record['KANTONSNUM']
        #add info
        
        
        commune_properties = {'name': commune_name,'canton_number': canton_number, 'commune_number': commune}
        
        
        commune_geometry = {'type': 'MultiPolygon', 'coordinates': [list(map(lambda x: list(x), commune_border))]}
        
        commune_dict = {'type': 'Feature','properties': commune_properties , 'geometry': commune_geometry}
        
        communes_final_dict['features'].append(commune_dict)
        
    return communes_final_dict


def fetch_canton_and_commune_boundaries():
    commune_sf = shapefile.Reader(COMUNES_PATH)
    canton_sf = shapefile.Reader(CANTON_PATH)
    cantons = fetch_cantons_dictionary_geojson(canton_sf)
    communes = fetch_communes_dictionary_geojson(commune_sf)
    return cantons,communes