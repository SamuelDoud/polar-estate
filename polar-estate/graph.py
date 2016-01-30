import json
import googlemaps
import math

class graph(object):
    """This class creates an object that represents a single graph and the data associated with that graph.
    This class does not attempt to analzye the data within it. It only offers up its display and its member's data"""
    def __init__(self, origin_address, types_of_interesting_points, max_distance):
        #max_distance does not have to be a distance, it could be a time-length
        #TODO: add an option for other transportation types (walking is clearly much different than driving
        self.key = "AIzaSyDFGVVkUy9ISBceeA6Y02ry0Q-Yagx3CEM"
        self.client = googlemaps.Client(self.key)
        self.address = origin_address
        self.types = types_of_interesting_points
        self.radius = max_distance #should be used to limit how far we search out
        self.geocode_base() #fetches the coordinates of this base address
        self.list_of_locations = self.get_locations()

    def geocode_base(self):
        self.lat_long = self.client.geocode(address=self.address)[0]['geometry']['location'] #god, this is ugly
    def get_locations(self):
        matrix = []
        for type_of in self.types:
            matrix.extend(self.get_locations_by_type(type_of))
        return matrix
    def get_locations_by_type(self,type_of_place):
        headers = ['Type', 'Name', 'lat_long','theta','rating', 'distance']
        names_of_places = self.client.places(type_of_place, location=self.lat_long, radius=self.radius)
        #print(names_of_places)
        lat_long_pairs = []
        total_structured_data = []
        for place in names_of_places['results']:
            temp = place['geometry']
            this_lat_long_pair = temp['location']
            lat_long_pairs.append(this_lat_long_pair)
            name = place['name']
            try:
                rating = place['rating']
            except:
                rating = 2.5 #middling value if it does not exist
            structured_data = [type_of_place]
            structured_data.append(name)
            structured_data.append(this_lat_long_pair)
            structured_data.append(self.get_theta(this_lat_long_pair))
            structured_data.append(rating)
            
            total_structured_data.append(structured_data)
        locations = self.client.distance_matrix(self.address, lat_long_pairs) #this gets the real distance of the places from the location
        row_data = locations['rows'][0]
        for index, location in enumerate(row_data['elements']):
            total_structured_data[index].append(location['distance']['value'])
        list_of_dicts = []
        for structured_data in total_structured_data:
            list_of_dicts.append(self.convert_to_dictionary(headers, structured_data))
        #print(locations)
        #print(names_of_places)
        return list_of_dicts

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

