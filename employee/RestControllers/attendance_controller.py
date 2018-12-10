from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.attendance import Attendance
from ..Serializers.attendance_serializer import AttendanceListSerializer,AttendanceDetailSerializer,AttendanceCreateSerializer


class AttendanceListView(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceListSerializer
    renderer_classes = [renderers.JSONRenderer]


class AttendanceDetailView(RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceDetailSerializer
    lookup_field = 'pk'
    renderer_classes = [renderers.JSONRenderer]


class AttendanceCreateView(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceCreateSerializer


class AttendanceUpdateView(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceDetailSerializer