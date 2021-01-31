import json
import geopandas as gpd

def GeoParsing(file):
    geodict={}
    count=0
    with open(file, 'r', encoding='utf-8') as geo:
        items = json.load(geo)
        features = items['features']
        for item in features:
            properties = item['properties']
            if properties['LINK_ID'] in geodict.keys():
                geodict[properties['LINK_ID']]=[geodict[properties['LINK_ID']], properties['F_NODE']]
                print(geodict[properties['LINK_ID']])
            else:
                geodict[properties['LINK_ID']]=properties['F_NODE']
                count+=1
    print(count)

file="./2019_09_20.geojson"
GeoParsing(file)