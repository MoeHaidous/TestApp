from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from myapp.models import Post, User
from myapp.serializer import UserSerializer
from myapp.views import RegisterUserAPIView,UserDetailAPI,AppView

# from myapp.views import AppView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', RegisterUserAPIView.as_view(),name='register'),
    # path('post/', AppView.as_view(),name='blog'),
    # path("get-details/",UserDetailAPI.as_view(), name='details'),
    path('api/token/', obtain_auth_token),
]
