import json

def GeoParsing(file):
    geolist=[]
    count=0

    with open(file, 'r', encoding='utf-8') as geo:
        items = json.load(geo)

        for index in range(0, len(items['features'])):
            value=items['features'][index]['geometry']['coordinates'][0]
            for idx, v in enumerate(value):
                if 126.803773>=v[0]>=126.336730 and 37.664078>=v[1]>=37.343033:
                    if len(value)-1 == idx:
                        geolist.append(items['features'][index]['properties']['LINK_ID'])
                        count+=1
                else:
                    break
    print(count)


file="./2019_09_20.geojson"
GeoParsing(file)