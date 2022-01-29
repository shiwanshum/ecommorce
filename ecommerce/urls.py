from django.urls import path, include
from .views import *

app_name = 'ecommerce'

urlpatterns = [

    # Product Related APIs

    path('product/',AllProductView.as_view()),           # view all product 

    path('product_create/', ProductCreate.as_view()),    # create product here

    path('productDetail/<int:id>/',ProductDetailAPI.as_view()), # view product detail

    path('product/<int:id>/',ProductUpdateAPI.as_view()),  # product update or delete
    
    
]