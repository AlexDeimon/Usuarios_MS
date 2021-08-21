from rest_framework import serializers
from .models import appUser
from django.contrib.auth.hashers import make_password
class appUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = appUser
        fields = ['id', 'username', 'password']
        
    def validate_password(self, value):
        return make_password(value)