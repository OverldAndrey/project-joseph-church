from django.urls import path
from django.contrib.auth import views as auth_views

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
    path('login/', views.login_user, name="login_user")
]