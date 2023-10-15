from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PrimaryUser)
admin.site.register(Transactions)
admin.site.register(Subscription)
admin.site.register(Wallet)