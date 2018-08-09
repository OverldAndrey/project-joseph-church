from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import ListView, DetailView
from joseph_app.models import Article

from . import views

app_name="joseph_app"
urlpatterns = [
    path('', views.index, name="index"),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('registration/', views.create_user, name="create_user"),
    path('reg_new_user/', views.register_user, name="register_user"),
    path('user_<int:user_pk>/profile/update', views.redact_user, name="redact_user"),
    path('user_<int:user_pk>/update', views.update_user, name="update_user"),
    path('user_<int:user_pk>/profile', views.user_cab, name="user_cab"),
    path('login/', views.login_user, name="login_user"),

    path('polls/', views.polls, name="polls"),
    path('polls/choice_reg_<int:user_pk>_<int:poll_pk>/', views.poll_choice_reg, name="poll_choice_reg"),
    path('news/',ListView.as_view(queryset=Article.objects.all().order_by('-date')[:20], template_name='joseph_app/many_articles.html')),
    path('news/<pk>',DetailView.as_view(model = Article, template_name = 'joseph_app/article.html')),
]
