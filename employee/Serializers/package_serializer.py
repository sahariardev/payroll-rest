from rest_framework.serializers import ModelSerializer
from ..Models.package import Package

class PackageListSerializer(ModelSerializer):
    class Meta:
        model=Package
        fields=['id','name','salary'];

class PackageDetailSerializer(ModelSerializer):
    class Meta:
        model=Package
        fields=['id','name','salary','annual_leave','sick_leave','extra','description'];

class PackageCreateSerializer(ModelSerializer):
    class Meta:
        model=Package
        fields=['name','salary','annual_leave','sick_leave','extra','description'];