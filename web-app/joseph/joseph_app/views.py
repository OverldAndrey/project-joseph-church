from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

from .models import User, Poll_choice, Poll, User_poll_choice, Event, Event_register, Article, Article_Image

import datetime
import os
import shutil
from docx import Document
from docx.shared import Inches
import openpyxl
from openpyxl.styles import Font

STATIC_PATH = os.getcwd()+"/joseph_app/static"
FILE_PATH = "/joseph_app/"

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

def logout_user(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse("joseph_app:login"))

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
    if request.FILES:
        f = request.FILES['avatar']
        path = STATIC_PATH+FILE_PATH+"userdata/{}/avatar/".format(user.pk)
        if not os.path.exists(path):
            os.mkdir(path[:-8])
            os.mkdir(path[:-1])
        with open(path+f.name, "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        user.avatar = path[len(STATIC_PATH):]+f.name
    if request.POST['date_of_birth']:
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
    return HttpResponsePermanentRedirect(reverse("joseph_app:login"))

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
        if request.FILES:
            f = request.FILES['avatar']
            path = STATIC_PATH+FILE_PATH+"userdata/{}/avatar/".format(user.pk)
            if not os.path.exists(path):
                os.mkdir(path[:-8])
                os.mkdir(path[:-1])
            else:
                os.remove(user.avatar)
            with open(path + f.name, "wb+") as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            user.avatar = path[len(STATIC_PATH):]+f.name
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

def password_change(request, user_pk):
    pwd = request.POST['password_old']
    email = request.user.email
    user = authenticate(request, username=email, password=pwd)
    if user is not None and user.is_authenticated:
        pwd1 = request.POST['password']
        pwd2 = request.POST['password_val']
        if pwd1 == pwd2:
            logout(request)
            user.set_password(pwd1)
            user.save()
        return HttpResponsePermanentRedirect(reverse("joseph_app:login"))

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

def poll_create(request, choice_number):
    new_poll = Poll(text=request.POST['text'], pub_date=datetime.datetime.now(), poll_type=request.POST['poll_type'])
    new_poll.save()
    if request.FILES:
        f = request.FILES['poll_image']
        path = STATIC_PATH + FILE_PATH + "poll_img/{}/".format(new_poll.pk)
        if not os.path.exists(path):
            os.mkdir(path[:-1])
        with open(path+f.name, "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        new_poll.poll_image = path[len(STATIC_PATH):]+f.name
    new_poll.save()
    for i in range(1,choice_number+1):
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
    if request.FILES:
        f = request.FILES['event_image']
        path = STATIC_PATH + FILE_PATH + "event_img/{}/".format(new_event.pk)
        if not os.path.exists(path):
            os.mkdir(path[:-1])
        with open(path+f.name, "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        new_event.image = path[len(STATIC_PATH):]+f.name
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

def make_docx(request, event_pk):
    document = Document()
    document.add_heading(Event.objects.get(pk=event_pk).title, 0)
    table = document.add_table(rows=1, cols=8)
    hd_row = table.rows[0].cells
    hd_row[0].text = "№"
    hd_row[1].text = "Имя"
    hd_row[2].text = "Фамилия"
    hd_row[3].text = "Электронная почта"
    hd_row[4].text = "Телефон"
    hd_row[5].text = "Вуз"
    hd_row[6].text = "Курс"
    hd_row[7].text = "Посещение"
    i = 0
    for reg in Event_register.objects.filter(event_pk=event_pk):
        data_row = table.add_row().cells
        data_row[0].text = str(i+1)
        data_row[1].text = reg.user.name
        data_row[2].text = reg.user.surname
        data_row[3].text = reg.user.email
        data_row[4].text = reg.user.phone
        data_row[5].text = reg.user.university
        data_row[6].text = str(reg.user.course)
        if reg.has_visited:
            data_row[7].text = "Посетил"
        else:
            data_row[7].text = "Отсутствовал"
        i += 1
    document.add_page_break()
    f = open("temp", mode="wb+")
    document.save(f.name)
    response = HttpResponse(f, content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response['content-disposition'] = "attachment; filename='event_brief_{}.docx'".format(event_pk)
    f.close()
    os.remove("./temp")
    return response

def make_xlsx(request, event_pk):
    wb = openpyxl.Workbook()
    wb.active.title = Event.objects.get(pk=event_pk).title
    tab = wb.get_sheet_by_name(wb.active.title)
    h_font = Font(size = 20)
    for l in "ABCDEFGH":
        tab[l+"1"].font = h_font
        tab.column_dimensions[l].width = 30
    tab["A1"] = "№"
    tab["B1"] = "Имя"
    tab["C1"] = "Фамилия"
    tab["D1"] = "Электронная почта"
    tab["E1"] = "Телефон"
    tab["F1"] = "Вуз"
    tab["G1"] = "Курс"
    tab["H1"] = "Посещение"
    i = 2
    for reg in Event_register.objects.filter(event_pk=event_pk):
        tab["A"+str(i)] = str(i-1)
        tab["B"+str(i)] = reg.user.name
        tab["C"+str(i)] = reg.user.surname
        tab["D"+str(i)] = reg.user.email
        tab["E"+str(i)] = reg.user.phone
        tab["F"+str(i)] = reg.user.university
        tab["G"+str(i)] = str(reg.user.course)
        if reg.has_visited:
            tab["H"+str(i)] = "Посетил"
        else:
            tab["H"+str(i)] = "Отсутствовал"
        i += 1
    f = open("temp", mode="wb+")
    wb.save(f.name)
    response = HttpResponse(f, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['content-disposition'] = "attachment; filename='event_brief_{}.xlsx'".format(event_pk)
    f.close()
    os.remove("./temp")
    return response

# Create your views here.

