import json
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from custom import serializers
from custom.serializers import UserSerializer, UserAccountSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import UserAccount
from corsheaders import conf


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(['POST'])
def Login(request):
    print(request)
    user = get_object_or_404(User, username=request.data['username'])
    account = get_object_or_404(UserAccount, owner=user)
    
    if user.check_password(request.data['password']):
        
        print(True)
        token , created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({"token": token.key, "user": serializer.data, 'accountId':account.pk})
    
    return Response({"detail":"password dont match"}, status=status.HTTP_400_BAD_REQUEST)
    # if not user.password == request.data['password'] :
    #     return Response({"detail":"user not found"}, status=status.HTTP_400_BAD_REQUEST)

    


@api_view(['POST'])
def Signup(request):
    print(dir(request))
    print(request.data)
    print(request.user)
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        token = Token.objects.create(user=user)

        userAccount = UserAccount.objects.create(
            date_of_birth=request.data['date_of_birth'],
            gender=request.data['gender'],
            country=request.data['country'],
            phone=request.data['phone'],
            fullname=request.data['fullname'],
            owner = user
            
        )
        userAccount.save()

        # subject = 'welcome to Stoxa'
        # message = f'Hi {user.username}, thank you for registering in Stoxa Stock exchange'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [user.email, email_from, ]
        # send_mail( subject, message, email_from, recipient_list )  

        return Response({ "token":token.key, "user": serializer.data })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def TestToken(request):
    print("token accessed")
    return Response("passed for {}".format(request.user.username))



@api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def UserAccountView(request):
    
    if request.method == 'POST':
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"user": serializer.data})
        else:
            return Response({"detail":"user not valid"}, status=status.HTTP_400_BAD_REQUEST)
    
    pk = request.GET.get('id')
    print(pk)

    user = UserAccount.objects.get(pk=pk)
    # if user.check_password(request.data['password']):
    #     print(True)
    #     return Response({"detail":"not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserAccountSerializer(instance=user)
    return Response({"user": serializer.data})
    




from .models import UserAccount
from .serializers import UserAccountSerializer
from rest_framework import generics


class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer