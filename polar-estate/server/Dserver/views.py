from django.shortcuts import render
from django.http import HttpResponse
from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
import ast

def page1(request): #name of the view = current_datetime
	html="this is a test"
	return HttpResponse(html)


def API(request): #name of the view = current_datetime
	request = str(request)

	#parse the query string 
	start = request.find('API')
	end = request.find("'",start)
	query_string = request[start:end]

	#this converts the string rep of the dict to 
	dict=ast.literal_eval(query_string)

	return HttpResponse(query_string)

	
