from django_filters import FilterSet
from .models import Product, ProductCategory, ProductInvectory, Discount

class ProuductFilterSet(FilterSet):

  class Meta:
    model = Product
    fields = {
       'id': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
       'name': ['exact', 'icontains'], 
       'category_id': ['exact', 'in'], 
       'inventory_id': ['exact', 'in'], 
       'price': ['exact', 'in'], 
       'discount_id': ['exact', 'in'], 
    } 

class ProuductCategoryFilterSet(FilterSet):

  class Meta:
    model = ProductCategory
    fields = {
       'id': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
       'name': ['exact', 'icontains'], 
    } 

class ProuductInvectoryFilterSet(FilterSet):

  class Meta:
    model = ProductInvectory
    fields = {
       'id': ['exact', 'in'],
       'quantity': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
    } 

class DiscountFilterSet(FilterSet):

  class Meta:
    model = Discount
    fields = {
       'id': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
       'name': ['exact', 'icontains'], 
       'discount_percent': ['exact', 'gte', 'lte'],
    } 