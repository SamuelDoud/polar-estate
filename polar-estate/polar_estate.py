import graph

#hello team, this is the "main" file of the backend
#I am just a holding class
#should I be the interface for the frontend-backend communications?
#probably a dispatcher
class ColectionDispatch(object):
    def __init__(self, base_address, target_addresses, types_of_locations, weights_for_types_of_locations, max_unit, time_or_distance):
        self.address = base_address
        self.types_of_locations = types_of_locations
        self.target_addresses = target_addresses
        self.weights_for_types_of_locations = weights_for_types_of_locations
        self.max_unit = max_unit
        self.list_of_maps = self.create_set_of_maps
        
    def create_set_of_maps(self):
        list_maps_objects = []
        for target_address in target_addresses:
            current_graph = graph(self.address, target_address)
            list_maps_object.append()
            
            
#Distance API key    
#AIzaSyDFGVVkUy9ISBceeA6Y02ry0Q-Yagx3CEM

#Places API key
#