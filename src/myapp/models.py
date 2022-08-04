import email
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    password = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name