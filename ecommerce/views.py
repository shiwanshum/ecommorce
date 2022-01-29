from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import viewsets, permissions, generics
from rest_framework.views import exception_handler
from rest_framework.response import Response
from .serializers import *
from .models import *
from .filter import ProductFilter
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
    search_fields = ["name"]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name','category','color','product_mrp',]
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