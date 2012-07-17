import csv, sqlite3, sys

def add_route(line,sql):
    columns=["passengers","freight","mail","carrier","carrier_name","src_id","src","dest_id","dest","year"]
    line=[e.replace("'","") for e in line]
    sqlstring="""INSERT INTO route VALUES({passengers}, {freight}, {mail}, '{carrier}',
    '{carrier_name}','{src}','{dest}',{year});""".format(**dict(zip(columns,line)))
    print sqlstring
    sql.execute(sqlstring)

conn=sqlite3.connect("../data/db/airports.sqlite")
sql=conn.cursor()
routes=csv.reader(open(sys.argv[1]))
print routes.next() #ignore first line

for line in routes:
    add_route(line,sql)

conn.commit()
conn.close()
