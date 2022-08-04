from django.shortcuts import render
from django.http import JsonResponse            #importing JsonResponse

#3rd party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView         #wrapper that creates an api view that accepts get and post methods
from rest_framework.response import Response     #inherets the json response

from .serializer import SignUpSerializer        #Utilizing the SignUpSerializer
from .models import Post                        #Utilizing the Post

class AppView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):    #used to handle a get request to the endpoint
        # app_data = {                            #creating a dictionary 
        # 'name' : 'Moe',
        # 'email' : 'Something@something.com',
        # 'password': 'Haidous'
        # }
        # return Response(app_data)
        users = Post.objects.all()
        serializer = SignUpSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):                              #sign up method to handle sign-up requests
        serializer = SignUpSerializer(data = request.data)                    #Passing data request into serializer

        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors)
