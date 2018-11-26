from django.db import models
from ..models import Package

class Bonus(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    amount = models.IntegerField()
    month = models.DateField()

