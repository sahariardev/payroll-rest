from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=30)
    salary = models.FloatField(null=False)
    annual_leave = models.IntegerField()
    sick_leave = models.IntegerField()
    extra = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name + "--" + str(self.salary) + "--" + str(self.annual_leave) + "--" + str(self.sick_leave)
