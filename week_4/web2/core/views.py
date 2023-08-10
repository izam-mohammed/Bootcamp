from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages

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

def index(request):
    if 'username' in request.session:
        return render(request, 'index.html')
    return redirect(login)

def logout(request):
    if 'username' in request.session:
        try:
            del request.session["username"]
        except:
            pass
    return redirect(login)