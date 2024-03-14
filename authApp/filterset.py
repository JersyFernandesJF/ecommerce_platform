from django_filters import FilterSet
from .models import User, UserPayment, UserAdress, ShoppingSession, CartItem, PaymentDetails, OrderDetails, OrderItems

class UserFilterSet(FilterSet):

  class Meta:
    model = User
    fields = {
       'id': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
       'user_name': ['exact', 'icontains'], 
       'first_name': ['exact', 'iconstains'],
       'last_name': ['exact', 'iconstains'],
       'category_id': ['exact', 'in'], 
       'inventory_id': ['exact', 'in'], 
       'number_phone': ['exact', 'in'], 
    } 

class UserPaymentFilterSet(FilterSet):

  class Meta:
    model = UserPayment
    fields = {
       'id': ['exact', 'in'],
       'user_id': ['exact', 'in'],
       'payment_type': ['exact', 'in'],
       'account_no': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
       'expiry': ['exact', 'icontains'], 
       'payment_type': ['exact', 'iconstains'],
    } 

class UserAdressFilterSet(FilterSet):

  class Meta:
    model = UserAdress
    fields = {
       'id': ['exact', 'in'],
       'user_id': ['exact', 'in'],
       'quantity': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
       'address_line1': ['exact', 'gte', 'lte'], 
       'address_line2': ['exact', 'gte', 'lte'], 
       'city': ['exact', 'gte', 'lte'], 
       'telephone': ['exact', 'gte', 'lte'], 
       'mobile': ['exact', 'gte', 'lte'], 
    } 

class ShoppingSessionFilterSet(FilterSet):

  class Meta:
    model = ShoppingSession
    fields = {
       'id': ['exact', 'in'],
       'user_id': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
       'total': ['exact', 'gte', 'lte'],
    } 

class CartItemFilterSet(FilterSet):

  class Meta:
    model = CartItem
    fields = {
       'id': ['exact', 'in'],
       'session_id': ['exact', 'in'],
       'product_id': ['exact', 'in'],
       'quantity': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
    }

class PaymentDetailsFilterSet(FilterSet):

  class Meta:
    model = PaymentDetails
    fields = {
       'id': ['exact', 'in'],
       'amount': ['exact', 'in'],
       'created_at': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
       'provider': ['exact', 'gte', 'lte'],
       'status': ['exact', 'gte', 'lte'],
    } 

class OrderDetailsFilterSet(FilterSet):

  class Meta:
    model = OrderDetails
    fields = {
       'id': ['exact', 'in'],
       'user_id': ['exact', 'in'],
       'total': ['exact', 'in'],
       'payment_id': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
    
    } 

class OrderItemsFilterSet(FilterSet):

  class Meta:
    model = OrderItems
    fields = {
       'id': ['exact', 'in'],
       'order_id': ['exact', 'in'],
       'product_id': ['exact', 'in'],
       'quantity': ['exact', 'in'],
       'payment_id': ['exact', 'gte', 'lte'], 
       'updated_at': ['exact', 'gte', 'lte'],
    
    } 