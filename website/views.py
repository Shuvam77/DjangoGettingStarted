from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner");

def date(request):
    return HttpResponse("This page was served at:" +str(datetime.now()));

def about(request):
    return HttpResponse("This is revist to this tutorial course to refresh the previously learned concept of django");

