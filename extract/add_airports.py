import sqlite3, csv

    
def insert_airport(line, sql):
    columns=["id","name","city","country","iata","icao","latitude","longitude","altitude","timezone","dst"]
    line=[e.replace("'","") for e in line]
    print(""" INSERT INTO airports VALUES ({id}, '{name}', '{city}',
    '{country}','{iata}','{icao}','{latitude}','{longitude}','{altitude}','{timezone}','{dst}');
        """.format(**dict(zip(columns,line))))
    sql.execute(""" INSERT INTO airports VALUES ({id}, '{name}', '{city}',
    '{country}','{iata}','{icao}','{latitude}','{longitude}','{altitude}','{timezone}','{dst}');
        """.format(**dict(zip(columns,line))))

conn=sqlite3.connect("../data/db/airports.sqlite")
sql=conn.cursor()
airports=csv.reader(open("../data/raw/airports.dat"))
for line in airports:
    insert_airport(line,sql)
conn.commit()
conn.close()
