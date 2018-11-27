from django.db import models

from .Employee import Employee


class GrantLeave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    duration = models.IntegerField(null=False,default=1)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    cause = models.TextField(null=False,default="not available")
    extra = models.TextField(null=True)

    def __str__(self):
        return self.employee.name + "--" + str(self.duration) + "--" + self.cause
