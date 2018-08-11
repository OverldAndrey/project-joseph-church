from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

from .models import User, Poll_choice, Poll, User_poll_choice, Event, Event_register, Article, Article_Image

import datetime

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

        reg_list = []
        for reg in user.event_register_set.all():
            reg_list.append(reg)
        event_list = []
        for event in user.event_register_set.all():
            event_list.append(Event.objects.get(pk=event.event_pk))

        response = {
            "user" : user,
            "reg_list" : reg_list,
            "event_list" : event_list,
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

def poll_create_page(request):
    return render(request, "joseph_app/poll_add.html")

def poll_create(request):
    new_poll = Poll(text=request.POST['text'], pub_date=datetime.datetime.now(), poll_type=request.POST['poll_type'])
    new_poll.save()
    for i in range(1,3):
        new_choice = Poll_choice(poll=new_poll, text=request.POST['poll'+str(i)])
        new_choice.save()
    return HttpResponsePermanentRedirect(reverse("joseph_app:polls"))

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

def events(request):
    user = request.user
    response = {
        "events_list" : Event.objects.all(),
        "user" : user,
    }
    return render(request, "joseph_app/events.html", response)

def event_create_page(request):
    return render(request, "joseph_app/event_add.html")

def event_create(request):
    new_event = Event(title=request.POST['title'], text=request.POST['text'], pub_date=datetime.datetime.now(),
                      event_date=request.POST['event_date'], place=request.POST['place'])
    new_event.save()
    return HttpResponsePermanentRedirect(reverse("joseph_app:events"))

def event_register(request, event_pk):
    user = request.user
    reg_token = Event_register(user=user, event_pk=event_pk)
    reg_token.save()
    return HttpResponsePermanentRedirect(reverse("joseph_app:events"))

def article_create_page(request):
    return render(request, "joseph_app/article_add.html")

def article_create(request):
    new_article = Article(title=request.POST['title'], body=request.POST['body'], date=datetime.datetime.now())
    new_article.save()
    return HttpResponsePermanentRedirect(reverse("joseph_app:news"))



# Create your views here.

