from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.designation import Designation
from ..Serializers.designation_serializer import DesignationListSerializer,DesignationDetailSerializer,DesignationCreateSerializer


class DesignationListView(ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationListSerializer
    renderer_classes = [renderers.JSONRenderer]


class DesignationDetailView(RetrieveAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationDetailSerializer
    lookup_field = 'pk'
    renderer_classes = [renderers.JSONRenderer]


class DesignationCreateView(CreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationCreateSerializer


class DesignationUpdateView(UpdateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationDetailSerializer