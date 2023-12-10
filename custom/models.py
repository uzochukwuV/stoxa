
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid


# Create your models here.


class UserAccount(models.Model):
    total_deposited =  models.IntegerField(null=True, blank=True, default=0)
    total_withdrawn = models.IntegerField(null=True, blank=True, default=0)
    stake = models.IntegerField(null=True, blank=True, default=0)
    trade = models.IntegerField(null=True, blank=True, default=0)
    plan_bonus = models.IntegerField(null=True, blank=True, default=0)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_account', blank=True, null=True)
    isPremium = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)





class Transactions(models.Model):
    listChoice = (
        ('Deposit', 'deposit'),
        ('Withdrawal', 'withdrawal')
    )

    transaction_type = models.CharField(choices=listChoice, max_length=100, blank=True, null=True)
    amount = models.IntegerField( blank=True, null=True)
    depositor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='depositor')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
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

class Wallet(models.Model):
    listChoice = (
        ('BTC', 'bitcoin'),
        ('ETH', 'etherum'),
         ('SOL', 'solana'),
          ('BNB', 'binance')
    )
    wallet_type = models.CharField(choices=listChoice, max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=225, blank=True, null=True)
    balance = models.IntegerField(verbose_name='balance')


class AccountInfo(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=225, blank=True, null=True)
    bank = models.CharField(max_length=225, blank=True, null=True)
    account_name = models.CharField(max_length=225, blank=True, null=True)


class Subscription(models.Model):
    listChoice = (
        ('Premium', 'Premium'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
        ('Bronze', 'Bronze'),
    )
    balance = models.IntegerField(default=0)
    sub_type = models.CharField(choices=listChoice, max_length=100, blank=True, null=True)
    subscriber = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='subscriber')
    

class Trader(models.Model):
    name = models.CharField(max_length=245, null=True, blank=True)
    activity = models.IntegerField(default=1)
    trade = models.IntegerField(default=1000)
    total_roi = models.IntegerField(default=4)


