from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm
from .models import Group, Profile
from wop.planner.forms import SignUpForm

# Create your views here.

def index(request):
    # print('user is', request.user)
    # user = User.objects.get(username=username)
    # groups = Group.objects.filter(user=user)
    # form= ()
    return render(request, 'index.html', {'user_loggedin': not request.user.is_anonymous})


def profile(request, username):
    user = User.objects.get(username=username)
    groups = Group.objects.filter(user=user)
    return render(request, 'profile.html', {'username':username, 'groups':groups })


# ===
# AUTH
# ===

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        print('POSTING to Login view')
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        print('form content', form)
        if form.is_valid():
            print('form is valid')
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                print('user is not none', user)
                if user.is_active:
                    print('user is active')
                    login(request, user)
                    print('logged in?????', request.user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/login')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/login')
    else:
        print('login get method')
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

