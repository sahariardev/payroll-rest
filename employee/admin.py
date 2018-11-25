from django.contrib import admin

from .Models.attendence import Attendence
from .Models.grantLeave import GrantLeave
from .models import Package,Type,Employee,Bonus


# Register your models here.
admin.site.register(Package)
admin.site.register(Type)
admin.site.register(Employee)
admin.site.register(Attendence)
admin.site.register(Bonus)
admin.site.register(GrantLeave)

