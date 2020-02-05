'''
closest_SW.py is a script showing just how easy it is to validate 
zip codes and calculate the distance from hard coded Steel Warehouse
locations.  It is not deployement grade yet but could be used to get
something up and ready fast and it is currently hard to test that 
without knowing more about SiSense applications.  

Key must be changed in production!

To use: import googlemaps and zipcodes using pip in python3
	pip install -U googlemaps
	pip install zipcodes

Call the program with: 
	python closest_SW.py #####
where the hashes are numbers reresenting a zip code

Tested in a Windows environment using Python 3.7.3
Modules: googlemaps 3.1.4, zipcodes 1.1.0
'''

import googlemaps, sys, zipcodes, operator

#key must be changed in production, currently linked to jobarr138@gmail.com
try:
	gmaps = googlemaps.Client(key="AIzaSyDOsomlxBC4RknkSMf_SnHyqkiy_vU5yok")
except:
	print("Problem with setting up Client in Google Maps")
	exit()

#program needs a zip code to function properly
try:
	zip = sys.argv[1]
except:
	print("Enter 5 digit zip code as a command line arguement")
	exit()
	
#checking if the zip code is valid
if(not zipcodes.matching(zip)):
	print("Invalid zip code")
	exit()
	
#scrape from file later, but for now we will hard code SW locations
loc_list = ["2722 West Tucker Drive, Box 1377 South Bend, Indiana 46624", 
			"6780 Water Way Drive Portage, Indiana 46368", 
			"535 West Forrest Hill Avenue Oak Creek, Wisconsin 49801",
			"4305 81st Avenue West Rock Island, Illinois 61201",
			"3193 Independence Road Cleveland, Ohio 44105",
			"4740 Hungerford Road Memphis, Tennessee 38118",
			"600 River Terminal Chattanooga, Tennessee 37406",
			"2141 E State Hwy 198 Osceola, Arkansas 72370",
			"100 Industrial Park Drive Calvert, Alabama 36513",
			"15355 Jacintoport Boulevard Houston, Texas 77015"]

result_list = []

for location in loc_list:
	#imperial is for proper units, otherwise it pulls kilometers
	result = gmaps.distance_matrix(location, zip, units="imperial")
	result_list.append(result)

distance_pairs = []

for res in result_list:
	location = res['origin_addresses'][0]
	
	#grab the raw string, to be converted into a float representing miles
	distance_str = res['rows'][0]['elements'][0]['distance']['text']
	
	#convert to float representing miles from searched zip code
	#makes sure all numbers are floats, without commas to avoid errors
	distance_float = float(distance_str[:distance_str.find(" ")].replace(',', ''))
	
	distance_pairs.append(tuple((location, distance_float)))
	
#sorts in place
distance_pairs.sort(key = operator.itemgetter(1))

#prints in order
for x in distance_pairs:
	print(x)

