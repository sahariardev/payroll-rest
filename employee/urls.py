
from django.urls import path
from django.conf.urls import url
from .RestControllers.employee_controller import EmployeeList,EmployeeSalary,EmployeeDetail,EmployeeCreate

urlpatterns = [

    url("employees/",EmployeeList.as_view(),name="employees"),
    url(r'^employee/(?P<pk>\d+)/$',EmployeeDetail.as_view(),name="employee"),
    url(r'^employee/create',EmployeeCreate.as_view(),name="create")
]