from django.db import models
import uuid
from django.utils import timezone

from .enums import PaymentType, PaymentStatus

# Create your models here.
class User(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key= True, null=False)
  user_name = models.CharField(max_length=40, null=False, blank=False)
  first_name = models.CharField(max_length=40, null=False, blank=False)
  last_name = models.CharField(max_length=40, null=False, blank=False)
  number_phone = models.CharField(max_length=17, null=False, blank=False)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)



class UserPayment(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True, null=False)
  user_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
  payment_type = models.CharField(choices=PaymentType.choices, null= True, blank=False, max_length= 16)
  provider = models.CharField(max_length=15, blank=True, null= True)
  account_no = models.IntegerField(blank=True, null= True)
  expiry = models.CharField(blank=True, null=True)



class UserAdress(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True, null=False)
  user_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
  address_line1 = models.CharField(max_length= 50, null=False, blank=False)
  address_line2 = models.CharField(max_length= 50, null=True, blank=False)
  city = models.CharField(max_length = 30, null=True, blank=False)
  telephone = models.CharField(max_length=30, blank=False)
  mobile = models.CharField(max_length=30, blank=False)


class ShoppingSession(models.Model):
  user_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
  total = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=3)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)



class CartItem(models.Model):
  session_id = models.ForeignKey('ShoppingSession', null=False, on_delete=models.CASCADE)
  product_id = models.ForeignKey('shoppingApp.Product', null=False, on_delete=models.CASCADE)
  quantity = models.IntegerField(null=False, blank=False)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)



class PaymentDetails(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True, null=False)
  amount = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=3)
  provider = models.CharField(max_length= 50, null=True, blank=False)
  status = models.CharField(choices=PaymentStatus.choices, null=True, blank=False,max_length=16)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)



class OrderDetails(models.Model):
  user_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
  total  = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=3)
  payment_id = models.ForeignKey('PaymentDetails', null=False, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)



class OrderItems(models.Model):
  order_id = models.ForeignKey('OrderDetails', null=False, on_delete=models.CASCADE)
  product_id = models.ForeignKey('shoppingApp.Product', null=False, on_delete=models.CASCADE)
  quantity = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=3)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)

