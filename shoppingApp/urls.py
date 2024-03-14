from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
   ProductCategoryViewSet, 
   ProductInvectoryViewSet, 
   ProductViewSet, 
   DiscountViewSet
)

default = DefaultRouter()
default.register('productCategory', ProductCategoryViewSet, basename='productCategory')
default.register('productInvectory', ProductInvectoryViewSet, basename='productInvectory')
default.register('product', ProductViewSet, basename='product')
default.register('discount', DiscountViewSet, basename='discount')


product = DefaultRouter()

urlpatterns = [
    path('shoppingApp/', include(default.urls)),

]