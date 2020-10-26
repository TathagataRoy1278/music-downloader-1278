from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from . import getmlink

# Create your views here.

def index(request):
	return render(request, "mainapp/index.html", {})

def result(request):
	search_query = request.GET['stext']
	link = getmlink.getlink(search_query)
	return render(request, "mainapp/result.html", {'link':link})
