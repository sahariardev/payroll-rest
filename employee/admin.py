from django.contrib import admin
from .Models.attendance import Attendance
from .Models.designation import Designation
from .Models.employee import Employee
from .Models.package import Package
from .Models.pay_head import PayHead
from .Models.pay_head_type import PayHeadType
from .Models.production_attendance_type import ProductionAttendanceType
from .Models.salary_detail import SalaryDetail
from .Models.salary_detail_item import SalaryDetailItem
from .Models.unit import Unit

admin.site.register(Attendance)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Package)
admin.site.register(PayHead)
admin.site.register(PayHeadType)
admin.site.register(ProductionAttendanceType)
admin.site.register(SalaryDetail)
admin.site.register(SalaryDetailItem)
admin.site.register(Unit)










