from django.urls import path, include
from .views import *

app_name = 'ecommerce'

urlpatterns = [

    # Product Related APIs

    path('product/',AllProductView.as_view()),           # view all product 

    path('product_create/', ProductCreate.as_view()),    # create product here

    path('productDetail/<int:id>/',ProductDetailAPI.as_view()), # view product detail

    path('product/<int:id>/',ProductUpdateAPI.as_view()),  # product update or delete
    

    # Categories Related APIs

    path('categories/',AllCategoriesView.as_view()),           # view all Categories 

    path('categories_create/', CategoriesCreate.as_view()),    # create Categories here

    path('categoriesDetail/<int:id>/',CategoriesDetailAPI.as_view()), # view Categories detail

    path('categories/<int:id>/',CategoriesUpdateAPI.as_view()),  # Categories update or delete
    
    
        # Size Related APIs

    path('size/',AllSizeView.as_view()),           # view all Sizes 

    path('size_create/', SizeCreate.as_view()),    # create Size here

    path('sizeDetail/<int:id>/',SizeDetailAPI.as_view()), # view Size detail

    path('size/<int:id>/',SizeUpdateAPI.as_view()),  # Size update or delete
    
        # Brand Related APIs

    path('brand/',AllBrandView.as_view()),           # view all Brands 

    path('brand_create/', BrandCreate.as_view()),    # create Brand here

    path('brandDetail/<int:id>/',BrandDetailAPI.as_view()), # view Brand detail

    path('brand/<int:id>/',BrandUpdateAPI.as_view()),  # Brand update or delete
]