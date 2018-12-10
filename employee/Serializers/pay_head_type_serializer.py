from rest_framework.serializers import ModelSerializer
from ..Models.pay_head_type import PayHeadType


class PayHeadTypeListSerializer(ModelSerializer):
    class Meta:
        model=PayHeadType
        fields=['id','name','description'];

class PayHeadTypeDetailSerializer(ModelSerializer):
    class Meta:
        model=PayHeadType
        fields=['id','name','symbol','description'];


class PayHeadTypeCreateSerializer(ModelSerializer):
    class Meta:
        model=PayHeadType
        fields=['name','description'];


