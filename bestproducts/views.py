from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(self):
	return HttpResponse("<h2>hello world you busted django</h2>")
def contact_view(self):
	return HttpResponse("<h1>hello world again</h1>")