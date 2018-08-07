from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="joseph_app"
urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('login/', views.login_user, name="login_user")
]