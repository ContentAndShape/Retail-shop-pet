from django.shortcuts import render
from django.http import HttpResponse

def index(request, name='index'):
    return(HttpResponse('Hello'))
