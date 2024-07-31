from django.db import models

# Create your models here.
from django.shortcuts import render
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser 
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.type = 'admin'
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)




class User(AbstractBaseUser, PermissionsMixin):
    TYPES = (
        ("doctor", "DOCTOR "),
        ("patient", "PATIENT"),
        )
    user_type=models.CharField(max_length=100,choices=TYPES, null=True,blank=True) #default='patient',
    first_name = models.CharField(max_length=50 , null=True,blank=True)
    last_name = models.CharField(max_length=50 , null=True , blank=True)
    profile=models.ImageField(default='default.jpg', upload_to='profile_images', null=True , blank=True)
    username=models.CharField(max_length=50 , null=True , blank=True)
    email = models.EmailField(('email address'), unique=True)
    
    password = models.CharField(max_length=100, blank=True, null=True)
    
    last_login = models.DateTimeField(verbose_name='last_login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

class Address(models.Model):
    line1=models.CharField(max_length=100 , null=True , blank=True)
    city=models.CharField(max_length=50 , null=True , blank=True)
    state=models.CharField(max_length=50 , null=True , blank=True)
    pincode=models.CharField(max_length=6 , null=True , blank=True)
    user=models.ForeignKey(User ,on_delete=models.CASCADE,null=True,blank=True)




