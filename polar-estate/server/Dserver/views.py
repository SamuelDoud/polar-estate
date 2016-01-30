from django.shortcuts import render
from django.http import HttpResponse
from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
import ast, sys, urllib

def page1(request): #name of the view = current_datetime
	html="this is a test"
	return HttpResponse(html)


def API(request): #name of the view = current_datetime
	request = str(request)

	#parse the query string 
	start = request.find('API')
	end = request.find("GET",start) - 2
	query_string = request[start+3:end]


	#decode the query string: note not all ASCII characheters can be encoded into URLS
	query_string = urllib.unquote(query_string).decode('ascii') 

	query_string = query_string.encode('ascii','ignore')

	#this converts the string rep of the dict to a dict
	dict=ast.literal_eval(query_string)
	print >> sys.stderr, "API Query: ", query_string

	return HttpResponse(query_string)

	
