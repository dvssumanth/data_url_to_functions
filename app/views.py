from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def data_from_url(request,man):
    return HttpResponse(f'hi {man} how are you')