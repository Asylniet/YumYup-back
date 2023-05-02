from django.db import models
from productt.models import Product


class Receipt(models.Model):
    name = models.CharField(max_length=355)
    process = models.TextField(max_length=6000)
    image = models.ImageField(upload_to='article/')

    def __str__(self):
        return f'{self.id}: {self.name}'


class Ingredient(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.FloatField(default=0)
    measure = models.FloatField(default=0)

    def __str__(self):
        return f'{self.id}: {self.product_id}'


class Ingredient_list(models.Model):
    receipt_id = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.receipt_id}: {self.ingredient_id}'
# Create your models here.
