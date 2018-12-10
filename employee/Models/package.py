from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=30)
    salary = models.FloatField(null=True)
    annual_leave = models.IntegerField()
    sick_leave = models.IntegerField()
    extra = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name