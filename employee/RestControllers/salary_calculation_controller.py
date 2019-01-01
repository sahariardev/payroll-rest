from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import renderers

from ..Models.salary_detail import SalaryDetail
from ..Serializers.salary_detail_serializer import SalaryDetailListSerializer



class SalaryCalculationTestView(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request, format=None):

        '''All data are avaialble on request.data
           get the data and then save one by one
        '''

        from_date=request.data.get('from_date')
        till_date=request.data['till_date']
        employee = request.data['employee']


        print(employee)

        salary_details=SalaryDetail.objects.all().filter( effective_from__gte = from_date).filter(employee__id=employee)
        #salary_details = SalaryDetail.objects.all().filter(employee__id=employee)
        serializer= SalaryDetailListSerializer(salary_details,many=True)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)