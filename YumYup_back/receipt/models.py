from django.db import models


class Receipt(models.Model):
    r_title = models.CharField(max_length=355)
    process = models.TextField(max_length=6000)
