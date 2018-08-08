from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

from .models import User

def index(request):
    return HttpResponse("Hale Joseph")

def login_user(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponsePermanentRedirect(reverse("joseph_app:user_cab", args=(user.pk,)))
    else:
        return HttpResponse("Login failed")

def create_user(request):
    response = {
        "user" : None
    }
    return render(request, "registration/update_user.html", response)

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
    return HttpResponsePermanentRedirect(reverse("joseph_app:login_user"))

def redact_user(request, user_pk):
    user = request.user
    if user is not None and user.is_authenticated and user.pk == user_pk:
        response = {
            "user" : user,
        }
        return render(request, "registration/update_user.html", response)

def update_user(request, user_pk):
    user = request.user
    if user is not None and user.is_authenticated and user.pk == user_pk:
        user.name = request.POST['name']
        user.surname = request.POST['surname']
        user.second_name = request.POST['second_name']
#        user.avatar =
        dob = request.POST['date_of_birth']
        user.date_of_birth = dob[6:]+"-"+dob[3:5]+"-"+dob[:2]
        user.phone = request.POST['phone']
        user.pubnet = request.POST['pubnet']
        user.university = request.POST['university']
        user.course = request.POST['course']
        user.reg_address = request.POST['reg_address']
        user.cur_address = request.POST['cur_address']
        user.organizations = request.POST['organizations']
        user.hobby = request.POST['hobby']
        user.save()
        return HttpResponsePermanentRedirect(reverse("joseph_app:user_cab", args=(user.pk,)))

def user_cab(request, user_pk):
    user = request.user
    if user is not None and user.is_authenticated and user.pk == user_pk:
        response = {
            "user" : user,
        }
        return render(request, "joseph_app/cabinet.html", response)
    else:
        return HttpResponsePermanentRedirect(reverse("joseph_app:login"))


# Create your views here.

