from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=30, null=False, blank=False)
  desc = models.CharField(max_length=280, null=False, blank=False)
  sku = models.CharField(max_length=30, null=True, blank=False)
  category_id = models.ForeignKey('ProductCategory', null=False, blank=False, on_delete=models.CASCADE)
  inventory_id = models.ForeignKey('ProductInvectory', null=False, blank=False, on_delete=models.CASCADE)
  price = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=3)
  discount_id = models.ForeignKey('Discount', null=False, blank=False, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)



class ProductCategory(models.Model):
  name = models.CharField(max_length=30, null=False, blank=False)
  desc = models.CharField(max_length=280, null=False, blank=False)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)



class ProductInvectory(models.Model):
  quantity = models.IntegerField(null=True, blank=False)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)



class Discount(models.Model):
  name = models.CharField(max_length=30, null=False, blank=False)
  desc = models.CharField(max_length=280, null=False, blank=False)
  discount_percent = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=3)
  active = models.BooleanField(null=False, default=False)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

