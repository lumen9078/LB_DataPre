import json

def GeoParsing(file):
    geolist=[]
    count=0

    with open(file, 'r', encoding='utf-8') as geo:
        items = json.load(geo)
        features = items['features']

        for value in features['geometry']['coordinates']:
            for index in len(value):
                if value[index][0]>126.336730 and value[index][0]<126.803773:
                    # print(value[0])
                    if value[index][1]>37.343033 and value[index][1]<37664078:
                        geolist.append(features['properties']['LINK_ID'])
                        count+=1
    print(count)

file="./2019_09_20.geojson"
GeoParsing(file)