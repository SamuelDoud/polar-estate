class graph(object):
    """This class creates an object that represents a single graph and the data associated with that graph.
    This class does not attempt to analzye the data within it. It only offers up its display and its member's data"""
    def __init__(self, origin_address, types_of_interesting_points, max_distance):
        #max_distance does not have to be a distance, it could be a time-length
        #TODO: add an option for other transportation types (walking is clearly much different than driving
        self.address = origin_address
        self.list_of_locations_indexed_by_type = self.get_all_locations
    def get_all_locations(self):
        """gets all the locations of all the types from a Google Maps API call (or set of calls). Returns a list of lists indexed by type of location"""
        for type_of_location in self.types_of_interesting_points:
            self.list_of_locations_indexed_by_type.append(super.get_locations(type_of_location)) #add the list of this type to the list of all lists   
    def get_locations(super, type_of_location):
        #get a list of a type (ex. gas station) from the origin address
        #be sure to cull by max_distance
    def create_polar_map(self):
        #create a map of the radius maxdistance

