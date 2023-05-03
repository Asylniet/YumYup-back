from django.db import models
from user.models import User
from receipt.models import Receipt


class Post(models.Model):
    receipt_id = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_photo/', blank=True)


class Rating(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    comment = models.TextField(max_length=5000)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


class Saved_post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


# Create your models here.
