from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import renderers
from rest_framework.viewsets import ViewSet
from ..Models.pay_head import  PayHead
from ..Serializers.pay_head_serializer import PayHeadCreateSerializer,PayHeadDetailSerializer,PayHeadListSerializer


class PayHeadListView(ListAPIView):
    queryset = PayHead.objects.all()
    serializer_class =PayHeadListSerializer
    renderer_classes = [renderers.JSONRenderer]


class PayHeadDetailView(RetrieveAPIView):
    queryset = PayHead.objects.all()
    serializer_class = PayHeadDetailSerializer
    renderer_classes = [renderers.JSONRenderer]


class PayHeadCreateView(CreateAPIView):
    queryset = PayHead.objects.all()
    serializer_class = PayHeadCreateSerializer
    #return the pk


class PayHeadTestView(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request, format=None):
        print("--------------------------")
        print("--------------------------")
        print(request.data)
        print(request.POST)
        print("--------------------------")
        return Response(request.POST)
class PayHeadTestViewSetView(ViewSet):
    renderer_classes = [renderers.JSONRenderer]
    def create(self,request):
        queryset = PayHead.objects.all()
        serializer = PayHeadCreateSerializer
        print("--------------------------")
        print("--------------------------")
        print(request.data)
        print(request.POST)
        print(serializer.data)
        print("--------------------------")
        return Response(serializer.data)

class PayHeadUpdateView(UpdateAPIView):
    queryset = PayHead.objects.all()
    serializer_class = PayHeadDetailSerializer