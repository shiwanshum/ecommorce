from django.urls import path
from .views import *
urlpatterns = [
    
    
    path('userdetails/<int:id>/',UserAPIView.as_view()),  # to view single details users 

    path('userlist/',UserListAPIView.as_view()),  # to view list of all users 

    path('userupdate/<int:id>/',UserUpdateAPIView.as_view()),  # update users or delete 
    
    path('rollcreate/',RollsCreate.as_view()),  # to view single details of rolls 
     
    path('rolldetails/<int:id>/',RollAPIView.as_view()),  # to view single details of rolls 
    
    path('rolllist/',RollsListAPIView.as_view()),  # to view list of all rolls 

    path('rollupdate/<int:id>/',RollsUpdateAPIView.as_view()),  # update users or delete rolls 
]