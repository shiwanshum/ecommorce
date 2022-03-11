from django.urls import path,re_path
from .views import *
from django.contrib.auth import views as auth_views
app_name='user'
urlpatterns = [
    
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('userdetails/<int:id>/',UserAPIView.as_view()),  # to view single details users 

    path('userlist/',UserListAPIView.as_view()),  # to view list of all users 

    path('userupdate/<int:id>/',UserUpdateAPIView.as_view()),  # update users or delete 
    
    path('rollcreate/',RollsCreate.as_view()),  # to view single details of rolls 
     
    path('rolldetails/<int:id>/',RollAPIView.as_view()),  # to view single details of rolls 
    
    path('rolllist/',RollsListAPIView.as_view()),  # to view list of all rolls 

    path('rollupdate/<int:id>/',RollsUpdateAPIView.as_view()),  # update users or delete rolls 
]