from django.db import models


class PayHeadType(models.Model):

    name=models.CharField(max_length=30, blank=False)
    description=models.TextField()

    def __str__(self):
        return self.name
