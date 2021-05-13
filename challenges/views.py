from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenge(request, month):
    challenge_text=None
    if month=='jan':
        challenge_text='Only vegetables in food!'
    elif month=='feb':
        challenge_text='Exercise daily!'
    elif month=='mar':
        challenge_text='Study aptitude daily!'
    else:
        return HttpResponseNotFound('No such a month found!')
    return HttpResponse(challenge_text)