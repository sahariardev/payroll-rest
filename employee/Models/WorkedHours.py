from django.db import models

from .Employee import Employee


class WorkedHours(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hours = models.IntegerField(null=False)
    rate = models.IntegerField(null=False)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.employee.name + "--" + str(self.hours) + "--" + str(self.rate) + "--" + self.currency
