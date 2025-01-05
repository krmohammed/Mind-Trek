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
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            clear_messages(request)
            messages.success(request, "Login Success")
            return redirect("quiz:quiz-home")
        else:
            clear_messages(request)
            messages.success(request, "Invalid Credentials")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def user_logout(request):
    clear_messages(request)
    messages.success(request, "Logout Success")
    logout(request)
    return redirect("/")
