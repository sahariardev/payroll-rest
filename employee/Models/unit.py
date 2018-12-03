from django.db import models

class Unit(models.Model):
    currency = models.TextField(max_length=20)
    tax = models.CharField(max_length=20)
    weight = models.TextField(max_length=10)
    height = models.TextField(max_length=10)
    time = models.TextField(max_length=10)
