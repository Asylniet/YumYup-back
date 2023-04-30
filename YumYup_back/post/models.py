from django.db import models
from users.models import User
from receipt.models import Ingredient_list


class Post(models.Model):
    receipt_id = models.ForeignKey(Ingredient_list, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Ratings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    comment = models.TextField(max_length=5000)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return f'{self.id}: {self.name}'


class Saved_post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.name}'


# Create your models here.
