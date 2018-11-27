from django.db import models

from employee.Models import employee


class Target(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    description = models.TextField(null=False)
    points = models.TextField(null=False)
    status = models.CharField(null=False)

    def __str__(self):
        return self.employee.name + "--" + self.points + "--" + self.status
