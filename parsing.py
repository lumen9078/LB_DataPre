import json

def SQLParsing(file):
    sql=open(file, 'r', encoding='UTF-8')
    par=open("./parsing.txt", 'w', encoding='UTF-8')
    line=str
    
    for s in sql:
        s=s.replace("\\", "")
        s=s.split("(")[1]
        s=s.split(")")[0]
        UUID=s.split("\'")[1]
        DATETIME=s.split("\'")[3]
        json_s=s.split("\'")[5]

        json_s=json.loads(json_s)

        for i in json_s:
            par.write(str(UUID) + "+" + str(DATETIME) + ":[")
            for index, value in enumerate(i['items']):
                if(index == len(i['items'])-1):
                    par.write("{lat:" + str(value['lat'])+ "," + "lng:" + str(value['lng']) + "}]\n")
                else:
                    par.write("{lat:" + str(value['lat'])+ "," + "lng:" + str(value['lng']) + "},\n")
    sql.close()
    par.close()

file="./TB_TRACKING2_DATA_20200222.sql"
SQLParsing(file)