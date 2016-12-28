from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user

from .forms import LoginForm


def login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(username=email, password=password)
            login_user(req, user)
            return redirect("home")

        return render(req, "users/login.html",
                      context={"form": form})

    else:
        form = LoginForm()
        return render(req, "users/login.html",
                      context={"form": form})

        # user = authenticate(...)
        # login(request, user)

def logout(req):
    pass
