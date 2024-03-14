from django.db import transaction
from rest_framework import serializers
from .models import Product, ProductCategory, ProductInvectory, Discount

class ProductSerializer(serializers.ModelSerializer):

  class Meta:
    model = Product
    fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):

  class Meta: 
    model = ProductCategory
    fields = '__all__'
  
class ProductInvectorySerializer(serializers.ModelSerializer):

  class Meta:
    model = ProductInvectory
    fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):

  class Meta:
    model = Discount
    fields = '__all__'
  
