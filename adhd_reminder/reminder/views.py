from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hi! This is our first project together :). Hope you enjoy. </h1>")