import json
import googlemaps
import math

class graph(object):
    """This class creates an object that represents a single graph and the data associated with that graph.
    This class does not attempt to analzye the data within it. It only offers up its display and its member's data"""
    def __init__(self, origin_address, types_of_interesting_points, max_distance):
        #max_distance does not have to be a distance, it could be a time-length
        #TODO: add an option for other transportation types (walking is clearly
        #much different than driving
        self.key = "AIzaSyDFGVVkUy9ISBceeA6Y02ry0Q-Yagx3CEM"
        self.client = googlemaps.Client(self.key)
        self.address = origin_address
        self.types = types_of_interesting_points
        self.radius = max_distance #should be used to limit how far we search out
        self.geocode_base() #fetches the coordinates of ths base address
        self.list_of_locations = self.get_locations()

    def geocode_base(self):
        self.lat_long = self.client.geocode(address=self.address)[0]['geometry']['location'] #god, this is ugly
    def get_locations(self):
        matrix = [] # this is the list of all the possible places.  This is not a member of the
                    # class!
        for type_of in self.types: #go through each seperate type
            matrix.extend(self.get_locations_by_type(type_of)) #add the new data to the matrix (a seperate type)
        return matrix
    def get_locations_by_type(self,type_of_place):
        headers = ['Type', 'Name', 'lat_long','theta','rating', 'distance'] #these are the ordered headers for the data...  key here on ordered.  Same
                                                                            #order as the structred_data list
        #this maybe should be refactored
        names_of_places = self.client.places(type_of_place, location=self.lat_long, radius=self.radius) #api call for this place type
        #print(names_of_places)
        lat_long_pairs = [] #this holds the lat long pair which will be needed in order collected to run
                            #the distance matrix
        total_structured_data = [] #this will hodl the dictionaries for each location
        for place in names_of_places['results']:
            geometry_data = place['geometry'] #geometry_data is whatever Google considers to be related to lat/long
            this_lat_long_pair = geometry_data['location']
            lat_long_pairs.append(this_lat_long_pair)
            total_structured_data.append(self.create_dictionary_from_place(place, type_of_place, this_lat_long_pair))
        locations = self.client.distance_matrix(self.address, lat_long_pairs) #this gets the real distance of the places from the location
        row_data = locations['rows'][0]
        for index, location in enumerate(row_data['elements']):
            total_structured_data[index]['distance'] = (location['distance']['value'])
        #print(locations)
        #print(names_of_places)
        return total_structured_data

    def create_dictionary_from_place(self, place, type_of_place, this_lat_long_pair):
        try: #rating is empty sometimes, make sure we can not crash.
            rating = place['rating']
        except:
            rating = 2.5 #middling value if it does not exist. Maybe we shouldn't even include these places seeing as they may be new or even "not real"
        another_dict = {}
        another_dict['type'] = type_of_place
        another_dict['name'] = place['name']
        another_dict['lat_long'] = this_lat_long_pair
        another_dict['theta'] = (self.get_theta(this_lat_long_pair))
        another_dict['rating'] = rating
        return another_dict

    def convert_to_dictionary(self,keys, values):
        conversion = {} #create a new dictionary
        for index, value in enumerate(values): #go through all the values
            conversion[keys[index]] = value #take the correspponding key, value pair and append it to a dictionary
        return conversion
    def get_theta(self, lat_long_dict):
        this_lat = self.lat_long['lat']
        this_lng = self.lat_long['lng']
        that_lat = lat_long_dict['lat']
        that_lng = lat_long_dict['lng']
        
        delta_lat = this_lat - that_lat
        delta_lng = this_lng - that_lng

        y = math.sin(delta_lng) * math.cos(this_lat)
        x = math.cos(that_lat) * math.sin(this_lat) - math.sin(that_lat)
        brng = math.atan2(y,x)
        return brng
#AIzaSyDFGVVkUy9ISBceeA6Y02ry0Q-Yagx3CEM

