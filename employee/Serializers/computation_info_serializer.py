from rest_framework.serializers import ModelSerializer,StringRelatedField
from ..Models.computation_info import ComputationInfo



class ComputationInfoListSerializer(ModelSerializer):
    pay_head=StringRelatedField()
    class Meta:
        model=ComputationInfo
        fileds=['id','pay_head','effective_from','effective_till_date']
class ComputationInfoDetailSerializer(ModelSerializer):
    pay_head = StringRelatedField()
    class Meta:
        model=ComputationInfo
        fileds=['id','pay_head','effective_from','effective_till_date','rule']
class ComputationInfoCreateSerializer(ModelSerializer):
    class Meta:
        model=ComputationInfo
        fileds=['pay_head','effective_from','effective_till_date','name']