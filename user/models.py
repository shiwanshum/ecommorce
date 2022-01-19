from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


# Create your models here.


GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=13,blank=True, null=True)
    address1 = models.TextField(max_length=200,blank=True, null=True)
    address2 = models.TextField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=20,blank=True, null=True)
    country = models.CharField(max_length=20,blank=True, null=True)
    pincode = models.IntegerField(null=True,blank=True)
    land_mark = models.CharField(max_length=60, blank=True)
    gender = models.CharField(max_length=12, choices=GENDER)
    is_customer = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return str(self.email)