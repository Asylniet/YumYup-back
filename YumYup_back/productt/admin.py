from django.contrib import admin
from productt.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'expires_in']
# Register your models here.
