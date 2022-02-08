from .models import *
import django_filters
from django_filters import DateRangeFilter,DateFilter



class ProductFilter(django_filters.FilterSet):
    product_mrp = django_filters.RangeFilter()
    class Meta:
        model = Product
        fields = ['name','categories','subcategories','brand','product_mrp','size']
        
        
class CategoriesFilter(django_filters.FilterSet):
    class Meta:
        model = Categories
        fields = ['categories_name','date','active']
        
        
class SubcategoriesFilter(django_filters.FilterSet):
    class Meta:
        model = Subcategories
        fields = ['subcategory','date','active']