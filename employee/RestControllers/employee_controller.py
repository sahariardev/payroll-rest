

from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..Models.employee import Employee
from ..Serializers.employee_serializer import EmployeeSerializer
from ..Service.salary_calculate_service import SalaryCalculateService

class EmployeeList(ListAPIView):
    #model added and data fetched
    employees=Employee.objects.all()
    #serializer added
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return self.employees
    def get(self, request, *args, **kwargs):

        print(type(args))
        print(type(kwargs))

        return self.list(request, *args, **kwargs)


class EmployeeSalary(RetrieveAPIView):

    employee=Employee.objects.get(pk=1)
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return self.employee
    def get(self, request, *args, **kwargs):
          return self.retrieve(request, *args, **kwargs)




