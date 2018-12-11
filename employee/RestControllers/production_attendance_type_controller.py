from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.production_attendance_type import ProductionAttendanceType
from ..Serializers.production_attendence_type_serializer import ProductionAttendanceTypeListSerializer,ProductionAttendanceTypeDetailSerializer,ProductionAttendanceTypeCreateSerializer


class ProductionAttendanceTypeListView(ListAPIView):
    queryset = ProductionAttendanceType.objects.all()
    serializer_class = ProductionAttendanceTypeListSerializer
    renderer_classes = [renderers.JSONRenderer]

class ProductionAttendanceTypeDetailView(RetrieveAPIView):
    queryset = ProductionAttendanceType.objects.all()
    lookup_field = 'pk'
    serializer_class = ProductionAttendanceTypeDetailSerializer
    renderer_classes = [renderers.JSONRenderer]

class ProductionAttendanceTypeUpdateView(UpdateAPIView):
    queryset = ProductionAttendanceType.objects.all()
    lookup_field = 'pk'
    serializer_class = ProductionAttendanceTypeDetailSerializer

class ProductionAttendanceTypeCreateView(CreateAPIView):
    queryset = ProductionAttendanceType.objects.all()
    serializer_class = ProductionAttendanceTypeCreateSerializer