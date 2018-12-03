from django.db import models

from .Employee import Employee


class Target(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.TextField(null=False)
    points = models.TextField(null=False)
    status = models.CharField(null=False,max_length=10)

    def __str__(self):
        return self.employee.name + "--" + self.points + "--" + self.status