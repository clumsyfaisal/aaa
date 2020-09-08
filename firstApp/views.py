from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    s = '<h1>Welcome to the First Django Application</h1>'
    return HttpResponse(s)
