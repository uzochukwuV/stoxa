from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


admin.site.register(Transactions)
admin.site.register(Subscription)
admin.site.register(Wallet)



