from django.contrib import admin
from .Models.attendence import Attendance
from .Models.designation import Designation
from .Models.employee import Employee
from .Models.package import Package
from .Models.pay_head import PayHead
from .Models.pay_head_type import PayHeadType
from .Models.production_attendence_type import ProductionAttendenceType
from .Models.salary_detail import SalaryDetail
from .Models.salary_detail_item import SalaryDetailItem
from .Models.unit import Unit
from .Models.computation_info import ComputationInfo
from .Models.unit_relation import UnitRelation

admin.site.register(Attendance)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Package)
admin.site.register(PayHead)
admin.site.register(PayHeadType)
admin.site.register(ProductionAttendenceType)
admin.site.register(SalaryDetail)
admin.site.register(SalaryDetailItem)
admin.site.register(Unit)
admin.site.register(ComputationInfo)
admin.site.register(UnitRelation)








