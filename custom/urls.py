from django.urls import path
from .views import *


urlpatterns = [
    path('', Home, name='home'),
    path('auth/', Login, name='login'),
    path('register/', Register, name='register'),
]