from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import login
from django.db import IntegrityError
from .models import User

# Create your views here.


def SignUp(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    elif request.method == "POST":
        if request.POST.get("password1") == request.POST.get("password2"):
            try:
                user = User.objects.create_user(
                    username=request.POST.get("email"),
                    first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    email=request.POST.get("email"),
                    password=request.POST.get("password1"),
                )
                user.set_second_name(request.POST.get("second_name"))
                user.set_phone(request.POST.get("phone"))
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "User already exists"},
                )
        else:
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm, "error": "Passwords did not match"},
            )
