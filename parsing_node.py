import json

def GeoParsing(file):
    geodict={}

    with open(file, 'r', encoding='utf-8') as geo:
        items = json.load(geo)
        features = items['features']
        count =0
        
        for item in features:
            properties = item['properties']
            if properties['F_NODE'] in geodict.keys():  # F_NODE가 geodict.keys에 있을 경우
                if type(geodict[properties['F_NODE']]) == str:  # F_NODE가 str인 경우
                    geolist=[]
                    geolist.append(geodict[properties['F_NODE']])   # key F_NODE안의 값을 list로 변경
                    geolist.append(properties['LINK_ID'])   # LINK_ID를 list에 추가
                    geodict[properties['F_NODE']]=geolist   # 해당 list의 값을 F_NODE를 key로 저장
                    # print(geodict[properties['F_NODE']])
                else:   # F_NODE가 list인 경우
                    geolist=geodict[properties['F_NODE']]   # key F_NODE는 이미 list이기 때문에 바로 저장 
                    geolist.append(properties['LINK_ID'])   # LINK_ID의 값을 list에 추가
                    geodict[properties['F_NODE']]=geolist   # 해당 list의 값을 F_NODE를 key로 저장
                    # print(geodict[properties['F_NODE']])
            else:   # F_NODE가 geodict.keys에 없을 경우
                geodict[properties['F_NODE']]=properties['LINK_ID']
                count+=1
        print(count)


file="./2019_09_20.geojson"
GeoParsing(file)