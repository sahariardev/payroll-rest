from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=False)

    def __str__(self):
        return self.type + "--" + self.description
