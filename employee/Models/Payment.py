from django.db import models

from employee.Models import Employee


class Payment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    amount_type = models.CharField(null=False, max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.employee.name + "--" + str(self.date) + "--" + str(self.amount) + "--" + self.amount_type
