from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("register/", views.user_registration, name="register"),
    path("login/", views.user_login, name="login"),
]
