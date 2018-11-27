from django.db import models

from .Type import Type
from .Package import Package


class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null=False)
    address = models.TextField(null=False)
    n_id = models.CharField(max_length=50, null=False, default=11111)
    phone_number = models.CharField(max_length=20, null=False, default="123456")
    email = models.EmailField(max_length=254,null=False,default='jhondoe@gmail.com')
    day_choices = tuple([tuple([i, i]) for i in range(32)])
    pay_day = models.IntegerField(choices=day_choices, default=1)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + "--" + self.email + "--" + self.package.name + "--" + self.type.name
