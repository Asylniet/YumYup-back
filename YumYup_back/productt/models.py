from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=355)
    expires_in = models.DateField()

    def __str__(self):
        return f'{self.id}: {self.name}'

# Create your models here.
