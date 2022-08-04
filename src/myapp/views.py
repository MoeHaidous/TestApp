from django.shortcuts import render
from django.http import JsonResponse            #importing JsonResponse
from django.contrib.auth.models import User

#3rd party imports
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.views import APIView         #wrapper that creates an api view that accepts get and post methods
from rest_framework.response import Response     #inherets the json response
from rest_framework.authentication import TokenAuthentication


from .serializer import UserSerializer,RegisterSerializer,BlogPostSerializer        #Utilizing the SignUpSerializer
from .models import Post
from myapp import serializer                        #Utilizing the Post

class AppView(APIView):

    def get(self, request, *args, **kwargs):    #used to handle a get request to the endpoint
        qs = Post.objects.all()
        post = qs.first()
        post = BlogPostSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):                              #sign up method to handle sign-up requests
        serializer = BlogPostSerializer(data = request.data)                    #Passing data request into serializer

        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors)


 #Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):

  
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

    # Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  def get(self,request, *args, **kwargs):
    user = User.objects.get(id=request.user.id)
    
    serializer = UserSerializer(user)
    return Response(serializer.data)

   