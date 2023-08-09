from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "january",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december"
}

# Create your views here.


def monthly_challenge(request, month):
    try:
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("Page not found")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month- 1] 
    return HttpResponseRedirect("/challenges/" + redirect_month)
