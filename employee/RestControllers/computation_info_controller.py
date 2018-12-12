from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import renderers
from ..Models.computation_info import ComputationInfo
from ..Serializers.computation_info_serializer import ComputationInfoListSerializer,ComputationInfoDetailSerializer,ComputationInfoCreateSerializer


class ComputationInfoListView(ListAPIView):
    queryset = ComputationInfo.objects.all()
    serializer_class = ComputationInfoListSerializer
    renderer_classes = [renderers.JSONRenderer]

class ComputationInfoDetailView(RetrieveAPIView):
    queryset = ComputationInfo.objects.all()
    lookup_field = 'pk'
    serializer_class = ComputationInfoDetailSerializer
    renderer_classes = [renderers.JSONRenderer]

class ComputationInfoUpdateView(UpdateAPIView):
    queryset = ComputationInfo.objects.all()
    lookup_field = 'pk'
    serializer_class = ComputationInfoDetailSerializer

class ComputationInfoCreateView(CreateAPIView):
    queryset = ComputationInfo.objects.all()
    serializer_class = ComputationInfoCreateSerializer