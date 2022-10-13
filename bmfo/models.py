from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# class CustomUser(AbstractUser):
# 	nickname = models.CharField(max_length=225)
# 	is_staff = models.BooleanField(default=False)
# 	USERNAME_FIELD = 'username'
# 	REQUIRED_FIELDS = []

# class Locker(models.Model):
# 	owner = models.ForeignKey(CustomUser)

class UserManager(BaseUserManager):
    def create_user(self, nickname, password, **extra_fields):
        user = self.model(
            nickname=nickname, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nickname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(nickname, password, **extra_fields) 


class CustomUser(AbstractBaseUser,PermissionsMixin):
	nickname = models.CharField(max_length=225,unique=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	USERNAME_FIELD = 'nickname'
	REQUIRED_FIELDS = []

	objects = UserManager()
 
class Product(models.Model):
	category = models.CharField(max_length=100)
	imgUrl = models.URLField(max_length=200)
	productId = models.AutoField(primary_key = True)
	name = models.CharField(max_length=100)
	price = models.IntegerField(max_length=20)
