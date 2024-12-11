from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100, name="username")
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="buyers")
