from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def jan(request):
    return HttpResponse("Only vegetables in food!")

def feb(request):
    return HttpResponse("Exercise daily!")