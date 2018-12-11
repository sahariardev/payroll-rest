from rest_framework.serializers import  ModelSerializer
from ..Models.production_attendance_type import ProductionAttendanceType


class ProductionAttendanceTypeListSerializer(ModelSerializer):
    class Meta:
        model=ProductionAttendanceType
        fields=['id','name','type']


class ProductionAttendanceTypeDetailSerializer(ModelSerializer):
    class Meta:
        model=ProductionAttendanceType
        fields = ['id', 'name', 'type']


class ProductionAttendanceTypeCreateSerializer(ModelSerializer):
    class Meta:
        model=ProductionAttendanceType
        fields = ['name', 'type']