sqlite3 airports.sqlite << EOF
create table airports (id integer, name varchar(100), city varchar(100),
country varchar(100), iata varchar(3), icao varchar(4), latitude real,
longitude, real, altitude integer, timezone integer, dst varchar (1));
create table route (passengers real, freight real, mail real, carrier
varchar(3), carrier_name varchar(50), src varchar(3), dest varchar(3), year
integer);
EOF
