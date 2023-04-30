from django.db import models
from products.models import Product


class Receipt(models.Model):
    name = models.CharField(max_length=355)
    process = models.TextField(max_length=6000)
    image = models.ImageField(upload_to='article/')

    class Meta:
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Ingredient(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.FloatField(default=1)
    measure = models.FloatField(default=10)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Ingredient_list(models.Model):
    receipt_id = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'


# # Create your models here.
