from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers 
from rest_framework.authtoken.models import Token
from user.models import  *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'mobile', 'password', 'is_customer', 'is_admin','is_staff')

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CustomRegisterSerializer(RegisterSerializer):
    is_customer = serializers.BooleanField()
    is_admin = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    mobile = serializers.CharField(max_length=12)

    class Meta:
        model = User
        fields = ('email', 'mobile', 'password', 'is_customer', 'is_admin','is_staff')

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'mobile': self.validated_data.get('mobile', ''),
            'is_customer': self.validated_data.get('is_customer', ''),
            'is_admin': self.validated_data.get('is_admin', ''),
            'is_staff': self.validated_data.get('is_staff', ''),
           
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_customer = self.cleaned_data.get('is_customer')
        user.mobile = self.cleaned_data.get('mobile')
        user.is_admin = self.cleaned_data.get('is_admin')
        user.is_staff = self.cleaned_data.get('is_staff')
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()
    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_customer = serializer_data.get('is_customer')
        is_admin = serializer_data.get('is_admin')
        is_staff = serializer_data.get('is_staff')
        return {
            'is_customer': is_customer,
            'is_admin': is_admin,
            'is_staff': is_staff,
        }