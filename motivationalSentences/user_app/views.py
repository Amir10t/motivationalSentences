from .models import User
from django.views.generic import View
from utils.email_service import send_email
from django.contrib.auth import login, logout
from django.utils.crypto import get_random_string
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, RegisterForm, ResetPassword




# Create your views here.

class LoginOrRegisterView(View):
    def get(self, request):
        login_form = LoginForm()
        register_form = RegisterForm()
        reset_password_form = ResetPassword()
        context = {
            "login_form": login_form,
            "register_form": register_form,
            "reset_password_form": reset_password_form
        }
        return render(request, "user/LoginOrSignUp.html", context)


def login_operator(request: HttpRequest):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        email = login_form.cleaned_data.get("email")
        password = login_form.cleaned_data.get("password")
        user: User = User.objects.filter(email=email).first()
        if(user is not None):
            if user.check_password(password):
                login(request, user)
            else:
                return HttpResponse("Pass is not Correct")
        else:
            return HttpResponse("There is No User")

        context = {
            "login_form":login_form
        }

        return render(request, "user/LoginOrSignUp.html", context)

def register_operator(request: HttpRequest):
    register_form = RegisterForm(request.POST)
    if (register_form.is_valid()):
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        repeat_password = register_form.cleaned_data.get("repeat_password")
        if User.objects.filter(email=email).exists() == False:
            if password == repeat_password:
                new_user = User(email=email)
                new_user.email_active_code = get_random_string(72)
                new_user.set_password(password)
                new_user.username = get_random_string(6)
                new_user.save()
            else:
                register_form.add_error("repeat_password", "pass != repeat pass")
        else:
            register_form.add_error("email", "Enter a new Email")

        context = {
            "register_from":register_form
        }

        return render(request, "user/LoginOrSignUp.html", context)


def reset_password_operator(request: HttpRequest):
    reset_password_form = ResetPassword(request.POST)
    if reset_password_form.is_valid():
        email = reset_password_form.cleaned_data.get("email")
        user: User = User.objects.filter(email=email).first()
        if(user is not None):
            user.email_active_code = get_random_string(72)
            send_email("Forgot Your Password?", f"If You Forgot Your Password Click on this link http://127.0.0.1:8000/reset-pass/{user.email_active_code}", email)
            return HttpResponse("Pass sent")
        else:
            return HttpResponse("There is No User")

class ResetPasswordView(View):
    def get(self, request:HttpRequest, active_code):
        user = User.objects.filter(email_active_code__iexact=active_code).first()
        login(request, user)
        return HttpResponse("LogIn!")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-or-register'))