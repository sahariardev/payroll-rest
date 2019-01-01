from rest_framework.serializers import ModelSerializer
from ..Models.pay_head import  PayHead

class PayHeadListSerializer(ModelSerializer):
    class Meta:
        model=PayHead
        fields=['id','name','calculation_type'];

class PayHeadDetailSerializer(ModelSerializer):
    class Meta:
        model=PayHead
        fields=['id','name','description','add_net_salary','calculation_type','rule','rate','calculation_period','pay_head_type','attendence_production_type','add_or_deduct','under'];

class PayHeadCreateSerializer(ModelSerializer):
    class Meta:
        model=PayHead
        fields = ['name', 'description', 'add_net_salary', 'rule','rate','calculation_type', 'calculation_period',
                  'pay_head_type', 'attendence_production_type', 'add_or_deduct', 'under'];