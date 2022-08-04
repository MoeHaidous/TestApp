from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from myapp.models import Post, User
from myapp.serializer import SignUpSerializer

from myapp.views import AppView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', AppView.as_view(), name= 'test'),
    path('api/token/',obtain_auth_token, name='obtain-token'),
]
