import sqlite3

class Airport():
    columns=[id,"name","city","country","iata","icao","latitude","longitude","altitude","timezone","dst"]
    additional=["passengers_left","passengers_arrived","freight_left","freight_arrived","mail_left","mail_arrived"]
    
    def __init__(self,line,sql):
        for (k,v) in dict(zip(columns,line)):
            self.__dict__[k]=v
        self.sql=sql
    
    def get_data(self):
        self.get_arriving()
        self.get_departing()
        
    def get_arriving(self):
        (self.passengers_arrived,self.freight_arrived,self.mail_arrived)=sql.execute("""SELECT
        sum(passengers),sum(freight),sum(mail) FROM route WHERE
        dest='%s';"""%self.iata).first()
        
    def get_departing(self):
        (self.passengers_left,self.freight_left,self.mail_left)=sql.execute("""SELECT
        sum(passengers),sum(freight),sum(mail) FROM route WHERE
        src='%s';"""%self.iata).first()
    

c=sqlite3.connect("../data/db/airports.sqlite")
sql=c.cursor()
airports=[Airport(line) for line in sql.execute("""SELECT * from airports WHERE iata IN (SELECT distinct (src) FROM route);""")]
for airport in airports:
    airport.get_data()

c.close()
