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
        fields = ["name","product_image1","product_image2","product_image3","product_image4","product_image5","product_image6","product_image7","product_image8","product_mrp","size","is_stock","id","brand","categories","product_mrp"]


class CategoriesDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model= Categories
        fields =["categories_name","active"]
        
        
class CategoriesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categories
        exclude=['active']
        
        
        
class CategoriesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categories
        fields ="__all__"
        
        
class SizeDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model= Size
        fields =["size","active"]
        
        
class SizeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Size
        exclude=['active']
        
        
        
class SizeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Size
        fields ="__all__"
        
        
        
class BrandDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields =["brand_name","logo_image","image",]
        
        
class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        exclude=['active','date']
        
        
        
class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields ="__all__"