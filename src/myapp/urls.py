from django.urls import path
from .views import AppView, UserDetailAPI,RegisterUserAPIView

urlpatterns = [
  path('register/',RegisterUserAPIView.as_view(),name='register'),
  path('get-details/',UserDetailAPI.as_view(), name='details'),
  path('blog-post/', AppView.as_view(),name='blog'),

  
]