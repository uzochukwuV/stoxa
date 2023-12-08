
from django.contrib import admin
from django.urls import path, include, re_path
from custom.restview import Login, Signup, TestToken, UserAccountView
from custom import restview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('custom.urls')),
    re_path('api/login', Login),
    re_path('api/signup', Signup),
    re_path('api/token', TestToken),
    path('snippets/', restview.UserAccountList.as_view()),
    path('snippets/<int:pk>/', restview.UserAccountDetail.as_view()),
]
