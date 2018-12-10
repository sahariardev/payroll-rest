

from django.conf.urls import url
from .RestControllers.employee_controller import EmployeeList,EmployeeSalary,EmployeeDetail,EmployeeCreate,EmployeeUpdate
from .RestControllers.unit_controller import  UnitListView,UnitDetailView,UnitCreateView,UnitUpdateView
from .RestControllers.package_controller import  PackageListView,PackageDetailView,PackageCreateView,PackageUpdateView
from .RestControllers.pay_head_controller import PayHeadListView,PayHeadCreateView,PayHeadDetailView,PayHeadUpdateView
from .RestControllers.salary_detail_controller import SalaryDetailListView,SalaryDetailDetailView,SalaryDetailUpdateView,SalaryDetailCreateView
from .RestControllers.salary_detail_item_controller import SalaryDetailItemListView,SalaryDetailItemDetailView, SalaryDetailItemUpdateView,SalaryDetailItemCreateView


urlpatterns = [

    url("employees/$",EmployeeList.as_view(),name="employees"),
    url(r'^employees/(?P<pk>\d+)/$',EmployeeDetail.as_view(),name="employee"),
    url(r'^employees/create/$',EmployeeCreate.as_view(),name="create"),
    url(r'^employees/(?P<pk>\d+)/edit/$',EmployeeUpdate.as_view(),name="update"),

    url("units/$", UnitListView.as_view(), name="units"),
    url(r'^units/(?P<pk>\d+)/$', UnitDetailView.as_view(), name="unit"),
    url(r'^units/create/$', UnitCreateView.as_view(), name="unit_create"),
    url(r'^units/(?P<pk>\d+)/edit/$', UnitUpdateView.as_view(), name="unit_update"),

    url("packages/$",PackageListView.as_view(),name="packages"),
    url(r'^packages/(?P<pk>\d+)/$',PackageDetailView.as_view(), name="package"),
    url(r'^packages/create/$', PackageCreateView.as_view(), name="package_create"),
    url(r'^packages/(?P<pk>\d+)/edit/$', PackageUpdateView.as_view(), name="package_update"),

    url("payheads/$", PayHeadListView.as_view(), name="payheads"),
    url(r'^payheads/(?P<pk>\d+)/$', PayHeadDetailView.as_view(), name="payhead"),
    url(r'^payheads/create/$', PayHeadCreateView.as_view(), name="payhead_create"),
    url(r'^payheads/(?P<pk>\d+)/edit/$', PayHeadUpdateView.as_view(), name="payhead_update"),

    url("salarydetails/$", SalaryDetailListView.as_view(), name="salarydetails"),
    url(r'^salarydetails/(?P<pk>\d+)/$', SalaryDetailDetailView.as_view(), name="salarydetails"),
    url(r'^salarydetails/create/$', SalaryDetailCreateView.as_view(), name="salarydetails_create"),
    url(r'^salarydetails/(?P<pk>\d+)/edit/$', SalaryDetailUpdateView.as_view(), name="salarydetails_update"),

    url("salarydetailitems/$", SalaryDetailItemListView.as_view(), name="salarydetails"),
    url(r'^salarydetailitems/(?P<pk>\d+)/$', SalaryDetailItemDetailView.as_view(), name="salarydetails"),
    url(r'^salarydetailitems/create/$', SalaryDetailItemCreateView.as_view(), name="salarydetails_create"),
    url(r'^salarydetailitems/(?P<pk>\d+)/edit/$', SalaryDetailItemUpdateView.as_view(), name="salarydetails_update")

]


