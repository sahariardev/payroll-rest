from rest_framework.serializers import ModelSerializer
from ..Models.attendance import Attendance


class AttendanceListSerializer(ModelSerializer):
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

