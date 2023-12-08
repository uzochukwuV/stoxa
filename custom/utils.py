
import random
from django.core.mail import EmailMessage


def generateOTP():
    otp =""
    for p in range(6):
        otp += str(random.randint(1,9))
    return otp

