from django.db import models
from .Package import Package

class Bonus(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE,null=True)
    amount = models.IntegerField()
    month = models.DateField()

    def __str__(self):
        return self.package.name+" amount {}".format(self.amount)

