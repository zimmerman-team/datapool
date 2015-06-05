# datapool
datapool orientdb main db


this is the repository of the datapool software

Requirements:
orientdb
python 2.7


What is datapool:

Datapool is a system where one can upload datafiles (csv,xml,json ..plus more to come) the system will analyse those files and store them in orient db.
Then the data can be linked to other data trough pivot points.
For example:

	Iata data has transaction information with dates and location,
	an other file has violent incidents per year and location
	through the pivot points , year and location data can be generated which shows the possible relation 
	between money spend and violent incidents per year fpor a certain location

the front end will include a query builder which makes it possible to visually see the data structures and click on the values you want 
and if you want to filter or aggregate them (SUM,AVG,MAX,MIN,MED)

The goal is to make it easy to analyze the combined data from different sources.

data can be private (only to be seen by the user whom uploaded it) or public (available to everyone).
We might build the option to share data with a team so that the team can use without it being public.


The data is stored in <a href="http://orientdb.com">orientDB</a> and relations between dataset is defined by edges to the pivot points.
the front end is being build in python with django as a frame work.








