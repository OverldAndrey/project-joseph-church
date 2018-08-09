from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

from .models import User, Poll_choice, Poll, User_poll_choice

def index(request):
    return HttpResponse("Hale Joseph")

#Логин пользователя, редирект на user_cab
def login_user(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponsePermanentRedirect(reverse("joseph_app:user_cab", args=(user.pk,)))
    else:
        return HttpResponse("Login failed")

#Создание нового пользователя, рендер страницы регистрации update_user.html
def create_user(request):
    response = {
        "user" : None
    }
    return render(request, "registration/update_user.html", response)

#Регистрация нового пользователя в базе данных, редирект на login_user
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

#Изменение информации о пользователе, рендер update_user.html
def redact_user(request, user_pk):
    user = request.user
    if user is not None and user.is_authenticated and user.pk == user_pk:
        response = {
            "user" : user,
        }
        return render(request, "registration/update_user.html", response)

#Изменение информации о пользователе в базе данных, редирект на user_cab
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

#Рендер страницы личного кабинета cabinet.html
def user_cab(request, user_pk):
    user = request.user
    if user is not None and user.is_authenticated and user.pk == user_pk:
        poll_list = []
        for poll in user.user_poll_choice_set.all():
            poll_list.append(Poll.objects.get(pk=poll.poll))
        choice_list = []
        for choice in user.user_poll_choice_set.all():
            if choice.choice:
                choice_list.append(Poll_choice.objects.get(pk=choice.choice))
            else:
                multiple_choices = []
                for choice_pk in choice.choice_mult.split("_"):
                    multiple_choices.append(Poll_choice.objects.get(pk=choice_pk))
                choice_list.append(multiple_choices)

        response = {
            "user" : user,
            "poll_list" : poll_list,
            "choice_list" : choice_list,
        }
        return render(request, "joseph_app/cabinet.html", response)
    else:
        return HttpResponsePermanentRedirect(reverse("joseph_app:login"))

def polls(request):
    user = request.user
    response = {
        "polls_list" : Poll.objects.all(),
        "user" : user
    }
    return render(request, "joseph_app/polls.html", response)

def poll_choice_reg(request, user_pk, poll_pk):
    user = request.user
    poll = Poll.objects.get(pk=poll_pk)
    if poll.poll_type == 1:
        choice = Poll_choice.objects.get(pk=request.POST[str(poll_pk)+'choice'])
        choice.votes += 1
        choice.save()
        user_choice = User_poll_choice(user=user, poll=poll.pk, choice=choice.pk)
        user_choice.save()
    elif poll.poll_type == 2:
        choice_list = request.POST.getlist(str(poll_pk)+'choice')
        for choice_pk in choice_list:
            choice = Poll_choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()
        user_choice = User_poll_choice(user=user, poll=poll.pk, choice_mult="_".join(choice_list))
        user_choice.save()

    return HttpResponsePermanentRedirect(reverse("joseph_app:polls"))



# Create your views here.

