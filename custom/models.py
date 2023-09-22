from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

# Create your models here.


class MyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    full_name       = models.CharField(max_length=500, blank=True, null=True)
    phone_number    = models.CharField(max_length=11, blank=True, null=True)
    city            = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth   = models.DateField(blank=True, null=True) 
    total_balance   = models.IntegerField(blank=True, null=True)
    profile_pics    = models.ImageField(upload_to='media', blank=True, null=True)
    country         = models.CharField(max_length=100, blank=True, null=True)
    isPremium       = models.BooleanField(default=False)
    isVerified      = models.BooleanField(default=False)
    account_number  = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Primary'
        

    def get_absolute_url(self):
        return reverse('primary', self.pk)
    
    def __str__(self) -> str:
        return f'{self.full_name}'


class Transactions(models.Model):
    listChoice = (
        ('Deposit', 'deposit'),
        ('Withdrawal', 'withdrawal')
    )

    transaction_type = models.CharField(choices=listChoice, max_length=100, blank=True, null=True)
    amount = models.IntegerField( blank=True, null=True)
    depositor = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='depositor')
    reciever = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='reciever')
    time_of_transaction = models.DateTimeField(auto_created=True, auto_now_add=True)
    unique_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    
    class Meta:
        verbose_name_plural = 'Transaction'

    def get_absolute_url(self):
        return reverse('user', self.pk)
    
    def __str__(self) -> str:
        return f'{self.transaction_type} {self.pk}'



