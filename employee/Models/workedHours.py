from django.db import models

from employee.Models.employee import Employee


class WorkedHours(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hours = models.IntegerField(null=False)
    rate = models.IntegerField(null=False)
    currency = models.CharField()

    def __str__(self):
        return self.employee.name + "--" + self.hours + "--" + self.rate + "--" + self.currency
