from rest_framework.serializers import ModelSerializer

from ..Models.attendance import Attendance
from ..Serializers.employee_serializer import EmployeeSerializerForOtherModels
from ..Serializers.production_attendence_type_serializer import  ProductionAttendanceTypeListSerializer
from ..Serializers.unit_serializer import UnitDetailSerializer

class AttendanceListSerializer(ModelSerializer):
    employee=EmployeeSerializerForOtherModels()
    unit=UnitDetailSerializer()
    production_attendance_type=ProductionAttendanceTypeListSerializer()
    class Meta:
        model=Attendance
        fields=['id','employee','production_attendance_type','value','unit'];


class AttendanceDetailSerializer(ModelSerializer):
    class Meta:
        model=Attendance
        fields=['id','employee','production_attendance_type','value','unit','date'];


class AttendanceCreateSerializer(ModelSerializer):
    class Meta:
        model=Attendance
        fields=['employee','production_attendance_type','value','unit','date'];


class AttendanceSerializerForSalaryCalculation(ModelSerializer):
    class Meta:
        model=Attendance
        fields=['value']
