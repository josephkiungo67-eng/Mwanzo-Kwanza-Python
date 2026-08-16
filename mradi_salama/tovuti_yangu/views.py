from django.shortcuts import render
from django.http import HttpResponse

def nyumbani(request):
    return HttpResponse("<h1>Karibu kwenye tovuti yangu ya kwanza salama ya Django!</h1>")


# Create your views here.
