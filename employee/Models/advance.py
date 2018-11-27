from django.db import models

from employee.Models import employee


class Advance(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    received = models.DateField(null=False)
    month = models.DateField()

    def __str__(self):
        return self.employee.name + "--" + str(self.amount) + "--" + str(self.received)
