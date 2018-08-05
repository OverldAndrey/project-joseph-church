from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hale Joseph")

# Create your views here.
