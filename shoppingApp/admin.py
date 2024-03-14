from django.contrib import admin
from .models import ProductCategory

@admin.register(ProductCategory)
class LocationAdmin(admin.ModelAdmin):
    list_product = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name')


