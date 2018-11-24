from django.db import models

# Create your models here.
#Package model
class Package(models.Model):
    name=models.CharField(max_length=30)
    annual_leave=models.IntegerField()
    sick_leave=models.IntegerField()
    extra=models.TextField()
    description=models.TextField()

    def __str__(self):
        return self.name

#Type Model
class Type(models.Model):
    type=models.CharField(max_length=30,unique=True)
    description=models.TextField(null=False)

    def __str__(self):
        return self.type

#model employees
class Employee(models.Model):
    name=models.CharField(max_length=30,null=False)
    address=models.TextField(null=False)
    n_id=models.CharField(max_length=30,null=False,default=11111)
    phone_number=models.CharField(max_length=20,null=False,default="123456")
    phone_number_secondary=models.CharField(max_length=20,null=True)
    day_choices=tuple([tuple([i,i]) for i in range(32)])
    pay_day=models.IntegerField(choices=day_choices,default=1)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,null=True)
    package=models.ForeignKey(Package,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

