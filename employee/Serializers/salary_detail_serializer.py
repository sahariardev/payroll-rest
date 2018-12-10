from rest_framework.serializers import ModelSerializer,StringRelatedField
from ..Models.salary_detail import SalaryDetail

class SalaryDetailListSerializer(ModelSerializer):
    class Meta:
        model=SalaryDetail
        employee = StringRelatedField()
        fields=['id','effective_from','effective_till_date','employee'];

class SalaryDetailSerializer(ModelSerializer):
    class Meta:
        model=SalaryDetail
        employee = StringRelatedField()
        fields = ['id', 'effective_from', 'effective_till_date', 'employee'];

class SalaryDetailSerializer(ModelSerializer):
    class Meta:
        model=SalaryDetail
        employee = StringRelatedField()
        fields = ['effective_from', 'effective_till_date', 'employee'];

