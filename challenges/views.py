from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

challenge ={
    'jan':'Only vegetables in food!',
    'feb':'Exercise daily!',
    'mar':'Study aptitude for a month!',
    'apr':'Practice coding'
}  


def monthly_challenge_number(request, month):
    months=list(challenge.keys())
    
    if month>len(months):
        return HttpResponseNotFound('No such a month found!')
    redirect_month=months[month-1]
    return HttpResponseRedirect('/challenges/'+redirect_month)
    
  
def monthly_challenge(request, month):
    try:
        challenge_text=challenge[month] 
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('No such a month found!')