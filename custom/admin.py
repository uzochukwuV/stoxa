from django.contrib import admin
from .models import MyUser, Transactions

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Transactions)