from  django.db import  models


class ProductionAttendenceType(models.Model):
    name=models.CharField(max_length=30,blank=False)
    type_choices=(
        ('Production','Production')
        ('attendence/leave with pay', 'attendence/leave with pay')
        ('attendence/leave without pay', 'attendence/leave without pay')
    )
    type=models.CharField(choices=type_choices)

    def __str__(self):
        return self.name

