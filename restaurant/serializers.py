from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Menu

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']