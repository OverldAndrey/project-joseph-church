from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hale Joseph")

def login_user(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Login successful")
    else:
        return HttpResponse("Login failed")

# Create your views here.
