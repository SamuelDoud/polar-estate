import graph
import polar_estate

base_addresses = ["4020 Calvert St. NW Washington DC", "4400 Massachusetts AVE NW Washington DC"]
types_of_locations = ["bars","parks", "chruches", "hospitals"]
max_radius = 8050 #about five miles
aggregate = polar_estate.ColectionDispatch(base_addresses, types_of_locations, [],max_radius, 0)
print(str(aggregate.list_of_dictionaries).encode('utf-8'))
