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


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def Login(request):
    user = get_object_or_404(User, username=request.data['username'])
    
    # if user.check_password(request.data['password']):
    #     print(True)
    #     return Response({"detail":"not found"}, status=status.HTTP_400_BAD_REQUEST)
    if not user.password == request.data['password'] :
        return Response({"detail":"not found"}, status=status.HTTP_400_BAD_REQUEST)

    token , created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def Signup(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        token = Token.objects.create(user=user)


        

        subject = 'welcome to Stoxa'
        message = f'Hi {user.username}, thank you for registering in Stoxa Stock exchange'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, email_from, ]
        send_mail( subject, message, email_from, recipient_list )  

        return Response({ "token":token.key, "user": serializer.data })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def TestToken(request):
    print("token accessed")
    return Response("passed for {}".format(request.user.username))



@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def UserAccountView(request, id):
    
    if request.method == 'POST':
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({"detail":"user not valid"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        
        user = UserAccount.objects.get(pk=id)
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