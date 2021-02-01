import json, datetime

def SQLParsing(file):
    sql=open(file, 'r', encoding='UTF-8')
    time={}
    
    for s in sql:
        s=s.replace("\\", "")
        s=s.split("(")[1]
        s=s.split(")")[0]
        UUID=s.split("\'")[1]
        DATETIME=s.split("\'")[3]
        json_s=s.split("\'")[5]

        json_s=json.loads(json_s)

        for i in json_s:
            value=[]
            for index, item in enumerate(i['items']):
                x = item['time']/1000
                value.append(SecondsConvertor(x))
            time[str(UUID) + "+" + str(DATETIME)]=value

    sql.close()

def SecondsConvertor(x):
    tm=datetime.datetime.fromtimestamp(int(x))
    tm_a=tm
    tm_a+=datetime.timedelta(minutes=5)
    tm_a-=datetime.timedelta(minutes=tm_a.minute%5, seconds=tm_a.second)
    return [str(tm), str(tm_a)]

file="./TB_TRACKING2_DATA_20200222.sql"
SQLParsing(file)