

from rest_framework.generics import ListAPIView
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




