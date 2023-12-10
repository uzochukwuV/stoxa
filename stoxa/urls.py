
from django.contrib import admin
from django.urls import path, include, re_path
from custom.restview import *
from custom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('custom.urls')),
    re_path('api/login', Login),
    re_path('api/signup', Signup),
    re_path('api/token', TestToken),
    path('snippets/', UserAccountList.as_view()),
    path('snippets/<int:pk>/', UserAccountDetail.as_view()),
    path('create/admin', views.createAdmin, name="createadmin")
]
