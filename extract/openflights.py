import csv,itertools

class Openflights(object):
    """ General openflights class """
    def __init__(self,d):
        for (k,v) in d.items():   
            self.__dict__[k]=v

class Airport(Openflights):
    """This class defines Airports and their properties:
        Airport(dict):
            dict - a dicitonary derived from the openflights database:
            keys: id, name, city, country, iata, icao, latitude, longitude,
            altitude, timezone, dst
    """ 

    def __init__(self,d):
        super(Airport,self).__init__(d)
        
class Route(Openflights):
    """This class defines routes and their properties:
        Route(dict):
            dict - a dictionary derived from the openflights database
    """        


class Airline(Openflights):
    """ This class defines Airlines and their properties:
        Airport(dict):
            dict - a dictionary derived from the openflights database
    """

class OfCollection(object):
    """ The genreral openflights collection object """

class Airports:
    """ this class takes the cvs from openflights.org and parses it. 
        Airports(fd):
            fd - file descriptor for the openflights.org csv
        
        methods:
            get(airport):
                returns airport
            
            add(airport):
                adds the airport to the set
            
            __iter__() and next ():
                Airports is iterable.
    """ 
    columns=["id","name","city","country","iata","icao","latitude","longitude"
        ,"altitude","timezone","dst"]
    def __init__(self,fd):
        airports=[Airport(dict(zip(self.columns,a))) for a in csv.reader(fd)]
        self.airports=dict([(a.iata,a) for a in airports])
    
    def add(self,airport):
        self.airports[airport.iata]=airport
    
    def get(self,iata):
        """ returns airport for code"""
        return self.airports[iata]
    
    def __iter__(self):
        self.index=-1
        return self
    
    def next(self):
        self.index+=1
        if self.index<len(self.airports):
            return self.airports.values()[self.index]
        else:
            raise StopIteration()

class Routes:
    """ this class takes a csv from openflights.org and parses it for
    routes.
    Routes(fd):
        fd - a file descriptor for the openflights.org csv
    
    methods:
        src(airport):
            get routes departing from airport

        dst(airport):
            get routes arriving at airport

        __iter__() and next():
            Routes is iterable
    """ 
    columns=["airline","airline_id" ,"source", "source_id",
        "destination","destination_id","codeshare","stops","equipment"]
    def __init__(self,fd):
        self.routes=[Route(dict(zip(self.columns,r))) for r in csv.reader(fd)]

    def src(self,airport,codeshare=True):
        if codeshare:
            return itertools.ifilter(lambda x: x.source==airport,self.routes)
        else:
            return itertools.ifilter(lambda x: (x.codeshare!="Y") & (
            x.source==airport), self.routes)
    
    def dst(self,airport,codeshare=True):
        if codeshare:
            return itertools.ifilter(lambda x: x.destination==airport,self.routes)
        else:
            return itertools.ifilter(lambda x: (x.codeshare!="Y") & (
            x.destination==airport), self.routes)
        
        
    def __iter__(self):
        self.index=-1
        return self
    
    def next(self):
        self.index+=1
        if self.index<len(self.routes):
            return self.routes[self.index]
        else:
            raise StopIteration()
        
if __name__=="__main__":
    csv_ap="http://openflights.svn.sourceforge.net/viewvc/openflights/openflights/data/airports.dat"
    csv_rt="http://openflights.svn.sourceforge.net/viewvc/openflights/openflights/data/routes.dat"
    import urllib2
    airports=Airports(urllib2.urlopen(csv_ap))
    routes=Routes(urllib2.urlopen(csv_rt))
    for a in airports:
        a.departures=len([r for r in routes.src(a.iata,codeshare=False)])
        a.arrivals=len([r for r in routes.dst(a.iata,codeshare=False)])
    md=max(airports,key=lambda x: x.departures)
    print "Most Departures: %s, %s, %s, %s"%(md.iata,md.name,md.city,md.country)

