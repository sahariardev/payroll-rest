from django.db import models

from employee.Models import Package


class Bonus(models.Model):
    description = models.TextField(null=False)
    amount = models.IntegerField()
    activation_date = models.DateField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.package + "--" + str(self.amount) + "--" + str(self.activation_date)
