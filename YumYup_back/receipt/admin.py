from django.contrib import admin
from .models import *


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('r_title', 'process')


# @admin.register(Ingredient)
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ('product_id', 'number', 'measure')
#
#
# @admin.register(Ingredient_list)
# class Ingredient_listAdmin(admin.ModelAdmin):
#     list_display = ('receipt_id', 'ingredient_id')
