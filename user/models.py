from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from datetime import date, datetime
from django.utils.translation import ugettext_lazy as _
# Create your models here.





class Rolls(models.Model):
    roll=models.CharField(max_length=30,blank=True,null=True)
    details=models.TextField(max_length=100,default="")
    active=models.BooleanField(default=True)
    add_date=models.DateTimeField(_('add date'),auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.roll
        
    class Meta:
        verbose_name_plural = 'User Rolls'

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=30, null=True,blank=True)
    mobile = models.CharField(max_length=13,blank=True, null=True)
    address1 = models.TextField(max_length=150,blank=True, null=True)
    address2 = models.TextField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=20,blank=True, null=True)
    country = models.CharField(max_length=20,blank=True, null=True)
    pincode = models.IntegerField(null=True,blank=True)
    roll =models.ManyToManyField("Rolls", verbose_name=('user_rolls'), default=None ,blank=True)
    land_mark = models.CharField(max_length=60, blank=True)
    gender = models.CharField(max_length=12, choices=GENDER,blank=True)
    is_customer = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    otp = models.IntegerField(null=True,blank=True)
    activation_key = models.CharField(max_length=150,blank=True,null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return str(self.email)
    
