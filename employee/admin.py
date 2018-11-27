from django.contrib import admin

from employee.Models import employee, bonus, attendance, grantLeave, package, type

# Register your models here.
admin.site.register(package)  # Salary Package
admin.site.register(type)   # Employee Type
admin.site.register(employee)   # Employee Entity
admin.site.register(attendance)
admin.site.register(bonus)
admin.site.register(grantLeave)
