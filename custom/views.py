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
from .models import *
from django.contrib.auth.hashers import make_password


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    


class LoginView(View):
    def get(self, request):
        print('login get request')
        return render(request, 'login/login.html')
    
    def post(self, request):
        print('login post request')
        
        email = request.POST['email']
        password = request.POST['password']

        
        user = authenticate(email=email, password=password)

        print(user.get_username())
        if user is not None:
            login(request, user)
            return redirect(reverse('account', args=['auth']))
        
        return render(request, 'login/login.html', {'email':email, 'password':password})


        

def Logout(request):
    logout(request)
    return redirect(reverse('home'))

class RegisterValidateEmailView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        email = data['email'] or ''

        if PrimaryUser.objects.filter(email=email).exists():
            return JsonResponse({'error':'email already exits'})
        
        return JsonResponse({'message':'not taken'})

class RegisterValidateUsernameView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        username = data['username'] or ''

        if PrimaryUser.objects.filter(username=username).exists():
            return JsonResponse({'error':'username already exits'})
        
        return JsonResponse({'message':'ok that\'s a great choice'})

class RegisterView(View):
    def get(self, request):
        return render(request, 'register/register.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        print(password)

        user = authenticate(password=password,email=email)
        print(user)

        if user is not None:
            return render(request, 'auth/signup.html', {'message':'user already exist'})
        else:
            print('user is none')
            
            new_user =PrimaryUser.objects.create(email=email,username=username, password=make_password(password))
            new_user.save()
            return redirect(reverse('login'))
        



class AccountPageView(View, mixins.LoginRequiredMixin):
    def get(self, request, auth):
        login = False
        if auth == 'auth':
            login = True

        return render(request, 'account/account_page.html', {'login': login})

    def post(self, request):
        return render(request)


class ProfileView(View, mixins.LoginRequiredMixin):
    def get(self, request, auth):
        return render(request)

    def post(self, request):
        return render(request)



class DepositView(View, mixins.LoginRequiredMixin):
    def get(self, request):
        return render(request)

    def post(self, request):
        return render(request)

class WithdrawPageView(View, mixins.LoginRequiredMixin):
    def get(self, request):
        return render(request, 'withdraw/withdraw.html')

    def post(self, request):
        pass

class AddBankPageView(View):
    def get(self , request):
        return render(request, 'deposit/deposit.html')
    

class Setting(View):
    def get(self, request):
        return render(request, 'setting/setting.html')
    


class TopTraderView(View):
    def get(self, request):
        return render(request, 'trader/trader.html')
    


class SubscriptionView(View):
    def get(self, request):
        return render(request, 'sub/sub.html')
    