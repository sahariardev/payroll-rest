from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
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



class PayHeadTestView(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request, format=None):

        '''All data are avaialble on request.data
           get the data and then save one by one
        '''
        return Response(request.POST,tatus=status.HTTP_201_CREATED)


class PayHeadUpdateView(UpdateAPIView):
    queryset = PayHead.objects.all()
    serializer_class = PayHeadDetailSerializer