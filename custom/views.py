from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import mixins


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    


class LoginView(View):
    def get(self, request):
        return render(request, 'login/login.html')
    
    def post(self, request):
        print('a hit')
        email = request.POST['email']
        password = request.POST['password']

        print(email + password)
        user = authenticate(password=password,email=email)
        print(user)
        if user is not None:
            login(user)
            print(user)
            return redirect(reverse('home'))
        return render(request, 'login/login.html', {'email':email, 'password':password})


        



class RegisterValidateEmailView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        email = data['email'] or ''

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error':'email already exits'})
        
        return JsonResponse({'message':'not taken'})

class RegisterValidateUsernameView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        username = data['username'] or ''

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error':'username already exits'})
        
        return JsonResponse({'message':'ok that\'s a great choice'})

class RegisterView(View):
    def get(self, request):
        return render(request, 'register/register.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        

        user = authenticate(username=username, password=password,email=email)

        if user is not None:
            return render(request, 'auth/signup.html', {'message':'user already exist'})
        else:
            print('user is not alvabkle')
            new_user =User.objects.create(username=username, password=password,email=email)
            new_user.save()
            return redirect(reverse('login'))
        



class AccountPageView(View, mixins.LoginRequiredMixin):
    def get(self, request):
        return render(request, 'account/account_page.html')

    def post(self, request):
        pass


class ProfileView(View, mixins.LoginRequiredMixin):
    def get(self, request):
        pass

    def post(self, request):
        pass



class DepositView(View, mixins.LoginRequiredMixin):
    def get(self, request):
        pass

    def post(self, request):
        pass

class WithdrawView(View, mixins.LoginRequiredMixin):
    def get(self, request):
        pass

    def post(self, request):
        pass