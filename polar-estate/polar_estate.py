import graph

#hello team, this is the "main" file of the backend
#I am just a holding class
#should I be the interface for the frontend-backend communications?
#probably a dispatcher
class CollectionDispatch(object):
    def __init__(self, base_addresses, types_of_locations, radius):
        self.base_addresses = base_addresses
        self.types_of_locations = types_of_locations
        self.weights_for_types_of_locations = weights_for_types_of_locations
        self.max_unit = max_unit
        self.list_of_dictionaries = self.create_set_of_maps()
        
    def create_set_of_maps(self):
        list_maps_objects = []
        for base_address in self.base_addresses:
            current_graph = graph.graph(base_address, self.types_of_locations, self.max_unit)
            list_maps_objects.append((base_address, current_graph.list_of_locations)) #make this a tuple with the base address and its locations as seperate tuples
        return list_maps_objects
            
            
#Distance API key    
#AIzaSyDFGVVkUy9ISBceeA6Y02ry0Q-Yagx3CEM

#Places API key
#