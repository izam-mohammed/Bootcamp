from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect(index)
        else:
            messages.add_message(request, messages.WARNING, "invalid credentials")
    return render(request, 'login.html')

@never_cache
def index(request):
    if 'username' in request.session:
        return render(request, 'index.html', context={'username': request.session['username']})
    return redirect(login)

def logout(request):
    if 'username' in request.session:
        try:
            del request.session["username"]
        except:
            pass
    return redirect(login)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password != password2:
            messages.add_message(request, messages.WARNING, 'Password not matching')
        elif User.objects.filter(username=username):
            messages.add_message(request, messages.WARNING, 'username is taken')
        elif User.objects.filter(email=email):
            messages.add_message(request, messages.WARNING, 'email is taken')
        else:
            user = User(username=username, email=email, password=password)
            user.save()
            request.session['username'] = username
            return redirect('/')
            
    return render(request, 'signup.html')
