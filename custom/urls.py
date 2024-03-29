from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('validate_email', csrf_exempt(RegisterValidateEmailView.as_view()), name='validate_email'),
    path('validate_username', csrf_exempt(RegisterValidateUsernameView.as_view()), name='validate_username'),
    path('account/<str:auth>/<int:pk>/', AccountPageView.as_view(), name='account'),
    path('addbank/', AddBankPageView.as_view(), name='addbank'),
    path('withdraw/', WithdrawPageView.as_view(), name='withdraw'),
    path('deposit/', DepositView.as_view(), name='deposit'),
    path('logout/', Logout, name='logout'),
    path('copy/', TopTraderView.as_view(), name='copy'),
    path('sub/', SubscriptionView.as_view(), name='sub'),
    path('currency/', CurrencyConverterView.as_view(), name='currency'),
    path('acccount/profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    


]