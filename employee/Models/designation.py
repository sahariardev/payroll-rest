from django.db import models

class Designation(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
