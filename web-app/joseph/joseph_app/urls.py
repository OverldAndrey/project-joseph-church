from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView
from joseph_app.models import Article

from . import views

app_name="joseph_app"
urlpatterns = [
    path('', views.index, name="index"),

    path('logout/', views.logout_user, name="logout_user"),
    path('registration/', views.create_user, name="create_user"),
    path('reg_new_user/', views.register_user, name="register_user"),
    path('user_<int:user_pk>/profile/update', views.redact_user, name="redact_user"),
    path('user_<int:user_pk>/update', views.update_user, name="update_user"),
    path('user_<int:user_pk>/update_password', views.password_change, name="password_change"),
    path('user_<int:user_pk>/profile', views.user_cab, name="user_cab"),
    path('login/', views.login_user, name="login_user"),

    path('polls/', views.polls, name="polls"),
    path('polls/choice_reg_<int:poll_pk>/', views.poll_choice_reg, name="poll_choice_reg"),
    path('polls/create/create_<int:choice_number>_poll', views.poll_create, name="poll_create"),

    path('news/', ListView.as_view(queryset=Article.objects.all().order_by('-date')[:20], template_name='joseph_app/news.html'), name="news"),
    path('news/create/create_article', views.article_create, name="article_create"),

    path('events/', views.events, name="events"),
    path('events/<int:event_pk>/register/', views.event_register, name="event_register"),
    path('events/visited/<int:reg_pk>', views.event_visited, name="event_visited"),
    path('events/create/create_event', views.event_create, name="event_create"),

    path('files/docx/<int:event_pk>', views.make_docx, name="make_docx"),
    path('files/xlsx/<int:event_pk>', views.make_xlsx, name="make_xlsx"),

    path('documents/', views.file_upload_page, name="file_upload_page"),
    path('documents/upload/', views.file_upload, name="file_upload"),
    path('documents/download/<int:doc_pk>', views.file_download, name="file_download"),

    path('application/retrieve/events', views.retrieve_event_list, name="retrieve_event_list"),
    path('application/retrieve/registers/<int:event_pk>', views.retrieve_reg_list, name="retrieve_reg_list"),
]
