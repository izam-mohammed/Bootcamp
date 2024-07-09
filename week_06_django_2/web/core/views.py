from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from random import choice

# Create your views here.

@never_cache
def login_user(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            if User.objects.filter(username=username):
                messages.add_message(request, messages.WARNING, 'Invalid password')
            else:
                messages.add_message(request, messages.WARNING, 'User not found')
    return render(request, 'login.html')

@never_cache
def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username):
                messages.add_message(request,messages.WARNING, "Username Exist")
            elif User.objects.filter(email=email):
                messages.add_message(request,messages.WARNING, "Email exist")
            else:
                password = make_password(password, salt=None, hasher="pbkdf2_sha256")
                user = User(username=username, email=email, password=password)
                user.save()
                user = authenticate(request ,username=username, password=password2)
                login(request, user)
                return redirect(index)          
        else:
            messages.add_message(request,messages.WARNING,"password not matching")
    return render(request, 'signup.html')

COLORS = ['rgb(203, 253, 173)','rgb(246, 190, 100)','rgb(174, 180, 243)', 'rgb(253, 173, 238)','rgb(175, 246, 255)','rgb(222, 189, 247)']

@never_cache
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/useradmin')
        return render(request, 'home.html', context={'user': request.user.username.title(), 'bg':choice(COLORS)})
    return redirect(login_user)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(login_user)

