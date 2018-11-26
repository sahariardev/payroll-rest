from django.db import models

from employee.Models import package


class Bonus(models.Model):
    description = models.TextField(null=False)
    amount = models.IntegerField()
    activation_date = models.DateField()
    package = models.ForeignKey(package, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.package + "--" + self.amount + "--" + self.activation_date
