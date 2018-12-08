from django.db import models


class Unit(models.Model):
    name=models.CharField(max_length=30, blank=False)
    symbol=models.CharField(max_length=10, blank=False)
    description=models.TextField()

    def __str__(self):
        return self.name
    