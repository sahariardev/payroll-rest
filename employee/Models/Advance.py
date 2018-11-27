from django.db import models

from .Employee import Employee


class Advance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    received = models.DateField(null=False)
    month = models.DateField()

    def __str__(self):
        return self.employee.name + "--" + str(self.amount) + "--" + str(self.received)
