from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def Home(request):

    return render(request, 'home/index.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email + "  " + password)

        primary = User.objects.all()
        print(primary)

        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return reverse('home', {'user': user})

    return render(request, 'login/login.html')

def Register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        user = authenticate(email=email, password=password)

    return render(request, 'auth/signup.html')