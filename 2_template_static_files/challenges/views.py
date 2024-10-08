import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())
    urls = {}
    for month in months:
        link = reverse('month-challenge',args=[month])
        urls[month]=link
    return render(request,"challenges/index.html",{
        "urls":urls,
        "months": months,

    })


def monthly_challenge_by_num(request, month):
    print(monthly_challenges.keys())
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Error, maximum month is 12</h1>")
    redirect_month = months[month - 1]
    # return HttpResponseRedirect(f"/challenges/{redirect_month}")
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # builds path /challenge/jan
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # Note:long way
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(
            request,
            "challenges/challenge.html",
            {"month": month,"text": challenge_text, },
        )
    except KeyError:
        raise Http404() #this function will find a 404.html in template folder
