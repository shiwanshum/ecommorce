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
    
         # Review Related API

    path('review/',ReviewAPIView.as_view()),  # Review create or list

    # Wishlist Related API

    path('addwishlist/',WishlistAPIView.as_view()),  # Review create or list

    path('delete_wishlit_item/<int:id>/',MyWishlistAPIView.as_view()),  # Review create or list

        # Delievery related API

    path('create_delevery_pincode/',CreateDeliveryPincodeAPIView.as_view()),  # Create delievery pincode 

    path('check_delevery_pincode/',CheckDeliveryPincodeAPIView.as_view()),  # Check delievery pincode 
     
      # Offer related APIs
     
    path('add_offer/',AddOfferAPIView.as_view()),  # Add offers api
    
    path('all_offer_user/',AllOfferAPIView.as_view()),  # All offers api Views of 
    
    path('all_offer_admin/',AllOfferAdminAPIView.as_view()),  # All offers api Views of admin
    

    path('offer_details/<int:id>/',OfferDetailAPIView.as_view()),  # Check offer details 
    
    
    
    
   # Bag related APIs

    path('additem_buy/',AddtoBuyBagView.as_view()),      # add item for buy in bag

    path('bag_view/', BagView.as_view()),                # view bag

    path('bag_view/<int:id>/', BagUpdateView.as_view()), #  bag update or delete item
    
    path('additem/',AddtoCartView.as_view()),
    path('removeitem/',RemoveFromCartView.as_view()),
    path('cartview/', CartView.as_view()),
        #order

    path('order_payment/',ConfirmPaymentAPIView.as_view()), # order create or payment
]