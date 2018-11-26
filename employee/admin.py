from django.contrib import admin

from employee.Models import employee, bonus, attendance, grantLeave, package, type

# Register your models here.
admin.site.register(package)
admin.site.register(type)
admin.site.register(employee)
admin.site.register(attendance)
admin.site.register(bonus)
admin.site.register(grantLeave)
