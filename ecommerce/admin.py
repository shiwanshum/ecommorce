from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Categories)
admin.site.register(Subcategories)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Review)
admin.site.register(Bag)
admin.site.register(DeliveryPincode)
admin.site.register(Offer)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderedBag)
admin.site.register(UserPayment)
admin.site.register(Items)

