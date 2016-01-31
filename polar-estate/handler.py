import polar_estate
import re

def handle(regex):
    regexStr = str(regex) #allows me to use autocomplete
    #this string starts with a paren and ends with one
    #eliminate them
    regexStr = regexStr.split('[', 4) #now this is a list
    ordered_data = []
    for i in range(1,4):
        ordered_data.append(clean(regexStr[i].split(','))) #order the data clean it
    return dispatch(ordered_data) #return the dispatched item defined by the dispatch funtion

def clean(list_of_str):
    #cleans the string by removing the characters that I find t be a nusiance
    for index, s in enumerate(list_of_str):
        list_of_str[index] = s.translate(str.maketrans(dict.fromkeys("\"[]"))) #removes these characters
    return list_of_str

def dispatch(ordered_data):
    dispatched_item = polar_estate.CollectionDispatch(ordered_data[0], ordered_data[1], ordered_data[1]) #creates an object with the ordered  data
    return dispatched_item #sends that object back to the handle function to return to the user
   
