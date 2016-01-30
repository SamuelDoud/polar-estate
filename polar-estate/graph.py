import json
import googlemaps

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
        self.radius = max_distance
        self.list_of_locations = self.get_locations()


    def get_locations(self):
        matrix = []
        for type_of in self.types:
            matrix = self.get_locations_by_type(type_of)

    def get_locations_by_type(self,type_of_place):
        names_of_places = self.client.places(type_of_place, location=self.address, radius=self.radius)
        print(names_of_places)
        lat_long_pairs = []
        total_structured_data = []
        for place in names_of_places['results']:
            structured_data = [type_of_place]
            temp = place['geometry']
            lat_long_pairs.append(temp['location'])
            name = place['name']
            try:
                rating = place['rating']
            except:
                rating = 2.5 #middling value if it does not exist
            structured_data.append(name)
            structured_data.append(lat_long_pairs[len(lat_long_pairs) - 1])
            structured_data.append(rating)
            total_structured_data.append(structured_data)
        locations = self.client.distance_matrix(self.address, lat_long_pairs) #this gets the real distance of the places from the location
        row_data = locations['rows'][0]
        for index, location in enumerate(row_data['elements']):
            total_structured_data[index].append(location['distance']['value'])
        print(locations)
        print(names_of_places)
#AIzaSyDFGVVkUy9ISBceeA6Y02ry0Q-Yagx3CEM

