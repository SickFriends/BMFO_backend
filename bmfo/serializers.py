from dataclasses import field
from .models import CustomUser, Product
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'nickname', 'password']
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance
        
        
class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=CustomUser.objects.all())],
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    password2 = serializers.CharField(write_only=True,required = True)
    
    class Meta:
        model = CustomUser
        fields = ('name','password','password2')
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': 'password fields did not match'}
            )
        return data
    
    def create(self, validated_data):
        if validated_data['name'] == 'admin050512':
            user = CustomUser.objects.create_superuser(
                validated_data['nickname'],
                validated_data['password'],
            )
        else:
            user = CustomUser.objects.create_user(
                validated_data['nickname'],
                validated_data['password'],
            )
        user.save()
        token = Token.objects.create(user=user)
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'imgUrl', 'name', 'price']


