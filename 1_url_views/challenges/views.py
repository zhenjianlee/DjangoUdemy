import logging

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse


# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

def index(request):
    months = list(monthly_challenges.keys())
    li_string=""
    for month in months:
        cap_month = month.capitalize()
        link = reverse("month-challenge",args=[month])
        li_string+=(f' <li> <a href="{link}"> {cap_month}</a></li> ')
        
    response_body=f"<ul>{li_string}</ul>"
    print(response_body)
    return HttpResponse(response_body)

def monthly_challenge_by_num(request,month):
    print(monthly_challenges.keys())
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Error, maximum month is 12</h1>")
    redirect_month=months[month-1]
    #return HttpResponseRedirect(f"/challenges/{redirect_month}")
    redirect_path= reverse("month-challenge",args=[redirect_month]) #builds path /challenge/jan
    return HttpResponseRedirect(redirect_path)

    
def monthly_challenge(request, month):
    try:
        return_data = monthly_challenges[month]
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    
    return_response = f"<h1>{return_data}</h1>"
    return HttpResponse(return_response)