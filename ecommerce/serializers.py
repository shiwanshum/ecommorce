from rest_framework import serializers
from .models import *
from user.models import User
from django.core.exceptions import ObjectDoesNotExist




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        exclude = ('quantity','is_active',)

'''class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = "__all__"'''

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields ="__all__"

class ProductDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ["name","product_image1","product_image2","product_image3","product_image4","product_image5","product_image6","product_image7","product_image8","product_mrp","size","is_stock","id","brand","category","product_mrp"]

