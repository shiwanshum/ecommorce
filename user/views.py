from django.shortcuts import render
from .models import *
from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import *
from rest_framework.response import Response
from .serializers import *
from datetime import datetime, timedelta,date
from rest_framework.generics import *

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def list(self, request, *args, **kwargs ):
        if not(request.user.is_admin == True ):
            return Response({"msg": "you have not permission to View list of all user ."}, status=401)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data, status=200) 
class UserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [permissions.IsAuthenticated,]
    lookup_field='id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_active==True):          
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
 
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"},status=400)
 
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)

class UserUpdateAPIView(RetrieveUpdateAPIView,DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    #permission_classes = [permissions.IsAuthenticated, ]
    lookup_field='id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_active==True):          
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
 
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"},status=400)
 
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)
    def put(self,request,*args,**kwargs):
        if not(request.user.is_active==True):
            
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
            if request.user.is_admin:
                pass
            elif not(instance.email==request.user.email):
                return Response({"NO_ACCESS": "Access Denied,Only user change own deatils"}, status=401)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"},status=400)
        serializer = self.get_serializer(instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=200)
    def destroy(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
            
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"},status=400)
        
        instance.is_active=False
        instance.releasing_date=datetime.now().date()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response({"SUCCESS": "Successfully Deleted"}, status=200)
    
    
    


class RollsCreate(CreateAPIView):
    queryset = Rolls.objects.all()
    serializer_class = RollDataSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def create(self, request, *args, **kwargs ):
        if not(request.user.is_admin == True):
            return Response({"msg": "you have not permission to create rolls"}, status=401)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200) 

    
class RollAPIView(RetrieveAPIView):
    queryset = Rolls.objects.all()
    serializer_class = RollDetailsSerializer
    permission_classes = [permissions.IsAuthenticated,]
    lookup_field='id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_active==True):          
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
 
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"},status=400)
 
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)
    
class RollsListAPIView(ListAPIView):
    queryset = Rolls.objects.all()
    serializer_class = RollDataSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def list(self, request, *args, **kwargs ):
        if not(request.user.is_admin == True ):
            return Response({"msg": "you have not permission to View list of all Rolls ."}, status=401)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data, status=200) 


class RollsUpdateAPIView(RetrieveUpdateAPIView,DestroyAPIView):

    queryset = Rolls.objects.all()
    serializer_class = RollUpdateSerializer
    #permission_classes = [permissions.IsAuthenticated, ]
    lookup_field='id'

    def retrieve(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):          
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
 
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"},status=400)
 
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=200)
    def put(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
            
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"},status=400)
        serializer = self.get_serializer(instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=200)
    def destroy(self,request,*args,**kwargs):
        if not(request.user.is_admin==True):
            
            return Response({"NO_ACCESS": "Access Denied"}, status=401)
        try:
            instance = self.queryset.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST":"Does not exist"},status=400)
        
        instance.active=False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response({"SUCCESS": "Successfully Deleted"}, status=200)