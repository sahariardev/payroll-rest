
from django.urls import path
from django.conf.urls import url
from .RestControllers.employee_controller import EmployeeList,EmployeeSalary,EmployeeDetail

urlpatterns = [

    url("employees/",EmployeeList.as_view(),name="employees"),
    url(r'^employee/(?P<pk>\d+)/$',EmployeeDetail.as_view(),name="employee")
]