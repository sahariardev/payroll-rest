from django.db import models

from employee.Models import employee


class GrantLeave(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    duration = models.IntegerField(null=False)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)
    cause = models.TextField(null=False)
    extra = models.TextField(null=True)

    def __str__(self):
        return self.employee.name + "--" + self.duration + "--" + self.cause + "--" + self.extra
