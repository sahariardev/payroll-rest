from django.conf.urls import url
from .RestControllers.employee_controller import EmployeeList, EmployeeSalary, EmployeeDetail,\
    EmployeeCreate, EmployeeUpdate
from .RestControllers.unit_controller import UnitListView,UnitDetailView,UnitCreateView,UnitUpdateView
from .RestControllers.package_controller import PackageListView, PackageDetailView,PackageCreateView, PackageUpdateView
from .RestControllers.pay_head_type_controller import PayHeadTypeListView, PayHeadTypeDetailView, PayHeadTypeCreateView,\
    PayHeadTypeUpdateView
from .RestControllers.attendance_controller import AttendanceListView, AttendanceDetailView,\
    AttendanceCreateView, AttendanceUpdateView


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

    url("payheadtypes/$",PayHeadTypeListView.as_view(),name="payheadtypes"),
    url(r'^payheadtypes/(?P<pk>\d+)/$',PayHeadTypeDetailView.as_view(), name="payheadtype"),
    url(r'^packages/create/$', PayHeadTypeCreateView.as_view(), name="payheadtypes_create"),
    url(r'^packages/(?P<pk>\d+)/edit/$', PayHeadTypeUpdateView.as_view(), name="package_update"),

    url("attendances/$",AttendanceListView.as_view(),name="attendances"),
    url(r'^attendances/(?P<pk>\d+)/$',AttendanceDetailView.as_view(), name="attendance"),
    url(r'^attendances/create/$', AttendanceCreateView.as_view(), name="attendance_create"),
    url(r'^attendances/(?P<pk>\d+)/edit/$', AttendanceUpdateView.as_view(), name="attendance_update"),
]


