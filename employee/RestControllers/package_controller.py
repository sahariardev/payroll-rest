from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.package import Package
from ..Serializers.package_serializer import PackageListSerializer,PackageDetailSerializer,PackageCreateSerializer

class PackageListView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageListSerializer
    renderer_classes = [renderers.JSONRenderer]

class PackageDetailView(RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageDetailSerializer
    lookup_field = 'pk'
    renderer_classes = [renderers.JSONRenderer]

class PackageCreateView(CreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageCreateSerializer

class PackageUpdateView(UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageDetailSerializer