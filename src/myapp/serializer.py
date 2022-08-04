from dataclasses import fields
from rest_framework import serializers
from .models import Post


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'name', 'email', 'password',
            )
