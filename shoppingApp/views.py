from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .filtersets import ( ProuductFilterSet, ProuductCategoryFilterSet, ProuductInvectoryFilterSet, DiscountFilterSet)
from .serializers import ( ProductSerializer, ProductCategorySerializer, ProductCategory, DiscountSerializer, ProductInvectorySerializer)
from .models import (Product, ProductCategory, ProductInvectory, Discount)


class ProductCategoryViewSet(ModelViewSet):
    authentication_classes = [] # TODO add authentications
    permission_classes = [] # TODO add permissions
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend, ProuductCategoryFilterSet]
    filterset_class = ProuductCategoryFilterSet
    queryset = ProductCategory.objects.all()
    ordering_fields = '__all__'

class ProductViewSet(ModelViewSet):
    authentication_classes = [] # TODO add authentications
    permission_classes = [] # TODO add permissions
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, ProuductFilterSet]
    filterset_class = ProuductFilterSet
    queryset = Product.objects.all()
    ordering_fields = '__all__'

class ProductInvectoryViewSet(ModelViewSet):
    authentication_classes = [] # TODO add authentications
    permission_classes = [] # TODO add permissions
    serializer_class = ProductInvectorySerializer
    filter_backends = [DjangoFilterBackend, ProuductInvectoryFilterSet]
    filterset_class = ProuductInvectoryFilterSet
    queryset = ProductInvectory.objects.all()
    ordering_fields = '__all__'

class DiscountViewSet(ModelViewSet):
    authentication_classes = [] # TODO add authentications
    permission_classes = [] # TODO add permissions
    serializer_class = DiscountSerializer
    filter_backends = [DjangoFilterBackend, DiscountFilterSet]
    filterset_class = DiscountFilterSet
    queryset = Discount.objects.all()
    ordering_fields = '__all__'

# Create your views here.


    