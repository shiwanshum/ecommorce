from rest_framework import serializers
from .models import *
from user.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import razorpay



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
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Review
        fields = '__all__'



class MyWishlistSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.email')
    product = ProductDisplaySerializer()

    class Meta:
        model = Wishlist
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Wishlist
        fields = '__all__'

class CheckDeliveryPincodeSerializer(serializers.ModelSerializer):
    available = serializers.ReadOnlyField()
    class Meta:
        model = DeliveryPincode
        fields = '__all__'

class PincodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryPincode
        fields = '__all__'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class AddOfferSerializer(serializers.ModelSerializer):
    today_product_mrp = serializers.ReadOnlyField()


    class Meta:
        model = Offer
        fields = '__all__'


class ViewAllOfferSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    product = ProductDisplaySerializer(read_only=True)
    class Meta:
        model = Offer
        fields = '__all__'


class OfferDetailSerializer(serializers.ModelSerializer):
    today_product_mrp = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    product = ProductDisplaySerializer(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'
        
        
        
        
        
        
        
        
        
        
        
        
        
class AddToBagSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    price = serializers.ReadOnlyField()
    orderid = serializers.ReadOnlyField()
    ordered = serializers.ReadOnlyField()
    payment_id = serializers.ReadOnlyField()

    class Meta:
        model = Bag
        fields = '__all__'

class ViewMyBagSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.email')
    item = serializers.ReadOnlyField()
    price = serializers.ReadOnlyField()
    orderid = serializers.ReadOnlyField()
    ordered = serializers.ReadOnlyField()
    payment_id = serializers.ReadOnlyField()
    #item = serializers.ReadOnlyField()

    class Meta:
        model = Bag
        fields = '__all__'
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['item'] = ProductNameSerializer(instance.item).data      

        return rep

class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields =  ['name','product_image1','size']
class BagProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'product_image1', 'product_mrp']
        
        
        
        
        
        
        
        
        
        
        
        
class ItemsCartSerializer(serializers.ModelSerializer):
    product = ProductDisplaySerializer(read_only=True)
    msg = serializers.SerializerMethodField(read_only=True)
    item_status = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Items
        fields = ["product","quantity","id","item_status","msg"]

    def get_msg(self,obj):

        if obj.product.is_stock==False:
            return "Out Of Stock"
        if obj.product.quantity - obj.quantity<0:
            return "You Can't buy this much quantity"
        return "Success"

    def get_item_status(self,obj):

        if obj.product.is_stock==False:
            return "out_of_stock"
        if obj.product.quantity - obj.quantity<0:
            return False
        return "in_stock"        



class CartSerializer(serializers.ModelSerializer):
    # order_id = serializers.SerializerMethodField(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    price = serializers.ReadOnlyField()
    orderid = serializers.ReadOnlyField()
    ordered = serializers.ReadOnlyField()
    payment_id = serializers.ReadOnlyField()
    item=ItemsCartSerializer(read_only=True,many=True)
    single_product=serializers.ReadOnlyField()
    class Meta:
        model = Bag
        fields='__all__'

    # def get_order_id(self, obj):

    #     amount =obj.amount

    #     if amount > 0:
    #         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    #         orderid = client.order.create(data={"amount": amount * 100, "currency": "INR", "payment_capture": "1"})
    #         obj.orderid = orderid["id"]

    #         obj.save()
    #     return None




