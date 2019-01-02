from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import renderers

from ..Models.salary_detail import SalaryDetail
from ..Serializers.salary_detail_serializer import SalaryDetailListSerializer
from  ..Models.attendance import Attendance
from ..Serializers.attendance_serializer import AttendanceSerializerForSalaryCalculation



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

        salary_details=SalaryDetail.objects.all().filter( effective_from__gte = from_date).filter(employee__id=employee).order_by()
        #salary_details = SalaryDetail.objects.all().filter(employee__id=employee)
        serializer= SalaryDetailListSerializer(salary_details,many=True)
        print(serializer.data)
        salary_detail_items=serializer.data[0]['salary_detail_item']

        for salary_detail_item in salary_detail_items:
            pay_head=salary_detail_item['pay_head']
            dbc=""
            if(pay_head['add_or_deduct']=='add'):
                dbc="Credited"
            else:
                dbc="Debited"

            if((pay_head['calculation_type'] =='On Production') or (pay_head['calculation_type'] =='On Attendence')):
                #find the attendances where date in range and employee and attendance ids are same

                attendance_id=pay_head['attendence_production_type']
                attendances=Attendance.objects.all().filter(employee__id=employee).filter(production_attendance_type__id=attendance_id).filter(date__gte=from_date).filter(date__lte=till_date)
                attendance_data_serializer=AttendanceSerializerForSalaryCalculation(attendances,many=True)
                print("--serialized data---")
                print(attendance_data_serializer.data)
                sum=0
                if(len(attendance_data_serializer.data) !=0):
                    for v in attendance_data_serializer.data:
                        print(v)
                        print(v['value'])
                        sum = sum + v['value']

                    print(sum)
                    print(pay_head)
                    final_amount = salary_detail_items['value'] * sum / salary_detail_items['rate']
                    print("---------------------------------------")
                    print(pay_head['description'])
                    print(dbc)
                    print(final_amount)
                    print("---------------------------------------")



        return Response(serializer.data,status=status.HTTP_201_CREATED)