from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from utils.utils import clear_messages


# Create your views here.
def user_registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            clear_messages(request)
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("users:login")
    else:
        formed = UserCreationForm()
        form = formed.render("users/reg_template.html")
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            clear_messages(request)
            messages.success(request, "Login Success")
            return redirect("/")
    else:
        formed = AuthenticationForm()
        form = formed.render("users/reg_template.html")
    return render(request, "users/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("/")
