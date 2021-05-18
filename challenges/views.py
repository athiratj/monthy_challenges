from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

challenge ={
    'january':'Only vegetables in food!',
    'february':'Exercise daily!',
    'march':'Study aptitude for a month!',
    'april':'Practice coding',
    'may': None,
}  

def index(request):
    months=list(challenge.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_number(request, month):
    months=list(challenge.keys())
    
    if month>len(months):
        return HttpResponseNotFound('No such a month found!')
    redirect_month=months[month-1]
    redirect_path=reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
  
def monthly_challenge(request, month):
    try:
        challenge_text=challenge[month] 
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()