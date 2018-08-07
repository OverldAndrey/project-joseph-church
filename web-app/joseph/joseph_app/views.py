from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse

from .models import User

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

def create_user(request):
    return render(request, "registration/new_user.html")

def register_user(request):
    user = User.objects.create_user(email=request.POST['email'], password=request.POST['password'])
    user.name = request.POST['name']
    user.surname = request.POST['surname']
    user.second_name = request.POST['second_name']
#    user.avatar =
    user.date_of_birth = request.POST['date_of_birth']
    user.phone = request.POST['phone']
    user.pubnet = request.POST['pubnet']
    user.university = request.POST['university']
    user.course = request.POST['course']
    user.reg_address = request.POST['reg_address']
    user.cur_address = request.POST['cur_address']
    user.organizations = request.POST['organizations']
    user.hobby = request.POST['hobby']
    user.save()
    return HttpResponse("Registered")

# Create your views here.
