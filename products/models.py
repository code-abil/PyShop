from django.db import models


# django.db --> Package
# models    --> Model
# Model     --> Class
# Product Class is inherited from Model Class.
class Product(models.Model):
    name = models.CharField(max_length=15)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    # 2083 is the standard max-limit for url.


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    discount = models.FloatField()
