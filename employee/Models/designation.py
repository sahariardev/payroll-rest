from django.db import models


class Designation(models.Model):

    name=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name