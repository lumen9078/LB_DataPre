import json

def SQLParsing(file):
    sql=open(file, 'r', encoding='UTF-8')
    par=open("./parsing.txt", 'w', encoding='UTF-8')
    
    for s in sql:
        s=s.replace("\\", "")
        par.write(s.split("\'")[1] + "+")
        s=s.replace("\"", "").split(",")

        for index, value in enumerate(s):
            if value.startswith('lat'):
                par.write("{" + value + ",")
            elif value.startswith('lng'):
                par.write(value + "},")
            elif value.startswith('(\''):    # UUID
                value=value.replace("(", "").replace("\'", "")
                par.write("]\n" + value + "+")
            elif value.startswith('\'['):
                pass
            elif value.startswith('\''):    # DATETIME
                value=value.replace("\'", "")
                par.write(value + ":[")
            else:
                pass
        par.write("]\n")

    sql.close()
    par.close()

file="./TB_TRACKING2_DATA_20200222.sql"
SQLParsing(file)