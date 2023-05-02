from rest_framework import serializers
from .models import *


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class Ingredient_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient_list
        fields = '__all__'