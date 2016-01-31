from django.shortcuts import render
from django.http import HttpResponse
from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
import ast, sys, urllib


def page1(request): #name of the view = current_datetime
	html="this is a test"
	return HttpResponse(html)

# The front end sends us an HTTP request. 
def API(request): #name of the view = current_datetime
	request = str(request)


	#parse the query string  
	#queries contain the following syntax: ....'PATH_INFO': u'/API{1:2,3:4,5:6}', 'PWD': '/User.... Thus we canculate the location of the dictionary, in this admittedly hacky way.
	#we could also use regex. Note that request.find("GET",start) means we find the first instance of "GET" after request[start] = A. 
	start = request.find('API') + 3
	end = request.find("GET",start) - 2

	print >> sys.stderr, request[start], request[end-1]

	if request[start] == '(' and request[end-1] == ')':
		query_string = request[start:end]


		#decode the query string: note not all ASCII characheters can be encoded into URLS
		query_string = urllib.unquote(query_string).decode('ascii') 

		query_string = query_string.encode('ascii','ignore')

		#this converts the string rep of the dict to a dict
		try:
			list=ast.literal_eval(query_string)
		except ValueError:
			return HttpResponse("improperly formatted list")

		print >> sys.stderr, "API Query: ", query_string


		#need to send this HTTP request to the Google API, and recieve HTTP response. 
			#-can be done by graph.py


		#Django needs to forward HTTP response to front end. 


		#each view you write is responsible for instantiating, populating and returning an HttpResponse.
		#what is returned here will be displayed on the user's desktop.
		return HttpResponse(query_string)

	else:
		return HttpResponse("null and/or void query")

	
