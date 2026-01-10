'''
Docstring for lat_long

when given the latitude and longitude coordinates, find whether 
the location is in the northern or southern hemishpere
and whether it is in the western or eastern hemisphere

inputs 
latitude and longitudes will be float values 
output - north west, north east , south west, south east 

equator and prime meridian won't be catered for
'''

lat = float(input("Latitude: "))
long = float(input("Longitude: "))

hemispere = ""

if lat > 0:
    hemispere += "North "
else:
    hemispere += "South "

if long > 0:
    hemispere += "East"
else:
    hemispere += "West"

print(hemispere)
 
