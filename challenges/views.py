from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    if (month == 'january'):
        return HttpResponse("This january!!")
    elif (month == 'february'):
        return HttpResponse("Wak for at least 20 minutes every day")
    else:
        return HttpResponseNotFound("Page not found")
