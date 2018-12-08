from django.db import models
from .unit import  Unit

class UnitRelation(models.Model):

    effective_from = models.DateField()
    effective_till_date = models.DateField()
    first_unit = models.IntegerField()
    value = models.FloatField()
    second_unit = models.IntegerField()

