from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenge_number(request, month):
    return HttpResponse(month)
    
challenge ={
    'jan':'Only vegetables in food!',
    'feb':'Exercise daily!',
    'mar':'Study aptitude for a month!',
    'apr':'Practice coding'
}    
def monthly_challenge(request, month):
    try:
        challenge_text=challenge[month] 
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('No such a month found!')