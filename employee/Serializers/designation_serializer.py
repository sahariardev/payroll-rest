from rest_framework.serializers import ModelSerializer
from ..Models.designation import Designation


class DesignationListSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = ['id', 'name', 'description'];


class DesignationDetailSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = ['id', 'name', 'description'];


class DesignationCreateSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = ['name', 'description'];


class DesignationIdNameSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = ['id', 'description'];
