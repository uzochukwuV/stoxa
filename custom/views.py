import math
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
        
        if request.user.is_authenticated:
            return redirect(reverse('account', args=['auth', request.user.pk]))
        return render(request, 'home/index.html')
    


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('account', args=['auth', request.user.pk]))
        return render(request, 'login/login.html')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        
        user = authenticate(email=email, password=password)

        
        if user is not None:
            login(request, user)
            return redirect(reverse('account', args=['auth',user.pk ]))
        
        return render(request, 'login/login.html', {'email':email, 'password':password, 'error':True})


        

def Logout(request):
    logout(request)
    return redirect(reverse('home'))

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


        user = authenticate(password=password,email=email)

        if user is not None:
            return render(request, 'auth/signup.html', {'message':'user already exist'})
        else:
            
            new_user =User.objects.create(email=email,username=username, password=make_password(password))
            new_user.save()
            return redirect(reverse('login'))
        



class AccountPageView(View, mixins.LoginRequiredMixin):
    def get(self, request, auth, pk):
        login = False
        if auth == 'auth':
            login = True

        randomNum = math.floor(7.9)
        
        
        user = User.objects.get(pk=pk)
        traders = Trader.objects.all()[:10]

        
        params = {
            'user':user,
            "login": login,
            "traders": traders
            }
        return render(request, 'account/index.html', {'params': params})
        

        
        

    def post(self, request):
        return render(request, '')


class ProfileView(View, mixins.LoginRequiredMixin):
    def get(self, request, pk):
        
        userProfile = User.objects.get(pk=pk)
        params = {
            'userProfile':userProfile
        }

        return render(request, 'profile/index.html', {'params':params})

    def post(self, request):
        return render(request, '')



class DepositView(View, mixins.LoginRequiredMixin):
    def get(self, request):
        return render(request, 'deposit/index.html')

    def post(self, request):
        return render(request, '')

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
    
class CurrencyConverterView(View):
    def get(self, request):
        return render(request, 'currency/index.html')

def createAdmin(request):
    if request.method == 'POST':
        Adminname = request.POST['Adminname']
        password = request.POST['password']
        key = request.POST['key']

        if key == '900':
            admin = User.objects.create_superuser(username=Adminname, email="admin@gmail.com", password=password)
            admin.save()
            return redirect(reverse('home'))
        else:
            return render(request, 'createAdmin.html')


    return render(request, 'createAdmin.html')
