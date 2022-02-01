from cgitb import lookup
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import viewsets, permissions, generics
from rest_framework.views import exception_handler
from rest_framework.response import Response
from .serializers import *
from user.permissions import *
from .models import *
from .filter import ProductFilter,CategoriesFilter
from user.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# from datetime import datetime, timedelta
# from rest_framework.views import APIView
# from django.contrib.auth import get_user_model
# User = get_user_model()
# import razorpay

# from .filter import *



class ProductPagination(PageNumberPagination):       
       page_size = 10

class AllProductView(ListAPIView):

    queryset = Product.objects.filter(is_active=True)
    search_fields = ["name","brand"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name','categories','color','product_mrp',]
    filterset_class = ProductFilter
    serializer_class = ProductDisplaySerializer
    lookup_field='id'
    pagination_class = ProductPagination
    

class ProductCreate(CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request):

        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)

        request.data['is_active']=True
        request.data['is_stock'] = True
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class ProductDetailAPI(RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.active==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)


class ProductUpdateAPI(RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.active==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)

    def partial_update(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        if not(request.user.active==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)
        instance.is_active=False
        instance.save()
        return Response({"Message": "Successfully Deleted"}, status=200)
    
    
    
    
    
class CategoriesPagination(PageNumberPagination):       
       page_size = 10

class AllCategoriesView(ListAPIView):

    queryset = Categories.objects.all()
    search_fields = ["categories_name"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['categories_name','date','active']
    filterset_class = CategoriesFilter
    serializer_class = CategoriesDisplaySerializer
    lookup_field='id'
    pagination_class = CategoriesPagination
    

class CategoriesCreate(CreateAPIView):

    queryset = Categories.objects.all()
    serializer_class = CategoriesCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request):

        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class CategoriesDetailAPI(RetrieveAPIView):

    queryset = Categories.objects.all()
    serializer_class = CategoriesUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)


class CategoriesUpdateAPI(RetrieveUpdateDestroyAPIView):

    queryset = Categories.objects.all()
    serializer_class = CategoriesUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)

    def partial_update(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)
        instance.active=False
        instance.save()
        return Response({"Message": "Successfully Deleted"}, status=200)
    
    


class AllSizeView(ListAPIView):

    queryset = Size.objects.all()
    search_fields = ["size"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['size','date','active']
    serializer_class = SizeDisplaySerializer
    lookup_field='id'
    

class SizeCreate(CreateAPIView):

    queryset = Size.objects.all()
    serializer_class = SizeCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request):

        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class SizeDetailAPI(RetrieveAPIView):

    queryset = Size.objects.all()
    serializer_class = SizeUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)


class SizeUpdateAPI(RetrieveUpdateDestroyAPIView):

    queryset = Size.objects.all()
    serializer_class = SizeUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)

    def partial_update(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)
        instance.active=False
        instance.save()
        return Response({"Message": "Successfully Deleted"}, status=200)
    
    
    
    
class AllBrandView(ListAPIView):

    queryset = Brand.objects.all()
    search_fields = ["brand_name"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['brand_name','date','active']
    serializer_class = BrandDisplaySerializer
    lookup_field='id'
    

class BrandCreate(CreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request):

        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class BrandDetailAPI(RetrieveAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)


class BrandUpdateAPI(RetrieveUpdateDestroyAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)

    def partial_update(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)
        instance.active=False
        instance.save()
        return Response({"Message": "Successfully Deleted"}, status=200)
    
    
    
    
    
    
    
    
class ReviewAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if Review.objects.filter(product=request.data.get('product'), user=self.request.user).exists():
            return Response({"ALREADY_EXIST": "Already have a review"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user))
        return Response(serializer.data, status=200)

class WishlistAPIView(ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        queryset = self.queryset.filter(user=user)
        if queryset.exists():
            serializer = MyWishlistSerializer(queryset, many=True, context={'request': request})
            return Response(serializer.data, status=200)
        else:
            return Response({"NO_ITEM": "Empty Bag"}, status=400)

    def create(self, request, *args, **kwargs):
        if Wishlist.objects.filter(product=request.data.get('product'), user=request.user).exists():
            return Response({"ALREADY_EXIST": "Item Already Exists in Wishlist"}, status=400)


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save())
        return Response(serializer.data, status=200)


class MyWishlistAPIView(RetrieveDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = MyWishlistSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class CreateDeliveryPincodeAPIView(ListCreateAPIView):
    queryset = DeliveryPincode.objects.all()
    serializer_class = PincodeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if DeliveryPincode.objects.filter(pincode=request.data.get('pincode'), available=True).exists():
            return Response({"ALREADY_EXIST": "Pincode Already Exists"}, status=200)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save())
        return Response(serializer.data, status=200)


class CheckDeliveryPincodeAPIView(ListCreateAPIView):
    queryset = DeliveryPincode.objects.all()
    serializer_class = CheckDeliveryPincodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if DeliveryPincode.objects.filter(pincode=request.data.get('pincode'), available=True).exists():
            return Response({"DELIVERY_AVAILABLE": "Delivery Available"}, status=200)
        else:
            return Response({"DELIVERY_NOT_AVAILABLE": "Delivery Not Available"}, status=400)
        
        
        
class AddOfferAPIView(ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = AddOfferSerializer
    pagination_class = ProductPagination
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def create(self, request, *args, **kwargs):
        # if Offer.objects.filter(product=self.request.data.get('product')).exists():
        #     return Response({"ALREADY_EXIST": "Product Already Exists in Offer "}, status=400)

        discount_percent = self.request.data.get('discount_percent')
        if float(discount_percent) > 100:
            return Response({"INCORRECT_VALUE": "Discount value s not more then 100"}, status=400)

        try:
            product = Product.objects.get(id=self.request.data.get('product'))
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Product Does not exist"}, status=400)

        

        current_product_mrp = product.product_mrp
        total_disc = (float(current_product_mrp) * float(discount_percent)/100)
        total_product_selling_mrp = (float(current_product_mrp) - float(total_disc))
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(
            serializer.save(today_product_mrp=total_product_selling_mrp)
        )
        return Response(serializer.data, status=200)


class OfferDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='id'
    
    
    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error":"Does not exist"},status=404)
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)

    def put(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        discount_percent = self.request.data.get('discount_percent')
        if float(discount_percent) > 100:
            return Response({"INCORRECT_VALUE": "Discount value s not more then 100"}, status=400)

        try:
            product = Product.objects.get(id=self.queryset.get(id=kwargs["id"]).product.id)
            
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Product Does not exist"}, status=400)

        

        current_product_mrp = product.product_mrp
        total_disc = (float(current_product_mrp) * float(discount_percent)/100)
        total_product_selling_mrp = (float(current_product_mrp) - float(total_disc))
        serializer.is_valid(raise_exception=True)
        serializer.save(today_product_mrp=total_product_selling_mrp)
        return Response(serializer.data, status=200)

    def destroy(self, request, *args, **kwargs):
        if not(request.user.is_admin==True):
                return Response({"error": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)
        instance.active=False
        instance.save()
        return Response({"Message": "Successfully Deleted"}, status=200)
    
    
class AllOfferAPIView(ListAPIView):

    queryset = Offer.objects.filter(active=True)
    search_fields = ["product"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['product','today_product_mrp','discount_percent','active']
    serializer_class = ViewAllOfferSerializer
    
class AllOfferAdminAPIView(ListAPIView):

    queryset = Offer.objects.all()
    search_fields = ["product"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['product','today_product_mrp','discount_percent','active']
    permission_classes = [IsAuthenticated,IsAdmin]
    serializer_class = ViewAllOfferSerializer
    