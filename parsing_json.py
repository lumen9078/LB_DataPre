import json

def SQLParsing(file):
    sql=open(file, 'r', encoding='UTF-8')
    par=open("./parsing.txt", 'w', encoding='UTF-8')
    
    for s in sql:
        s=s.replace("\\", "")
        s=s.replace(")", "").split("(")
        dex=0

        for items in s:
            if 'INSERT' in items:
                pass
            else :
                items=items.split("\'")
                par.write(items[1] + "+" + items[3] + ":[")
                items=items[5]
                items=json.loads(items)
                for value in items:
                    items=value
                for index, value in enumerate(items['items']):
                    if(index == len(items['items'])-1):
                        par.write("{lat:" + str(value['lat'])+ "," + "lng:" + str(value['lng']) + "}]\n")
                    else:
                        par.write("{lat:" + str(value['lat'])+ "," + "lng:" + str(value['lng']) + "},")
    sql.close()
    par.close()

file="./TB_TRACKING2_DATA_20200222.sql"
SQLParsing(file)