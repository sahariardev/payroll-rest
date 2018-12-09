from ..Models.employee import Employee
from ..Models.attendence import Attendance



class SalaryCalculateService():


    def  calculateSalaryForOneEmployee(self,employee_id):
        '''basically calculates the emplyee earnings'''
        '''Check the employee type. If the type does not match with the Employee throw type mismatch exception'''
        '''find the activated salary details of the particular employee using date
           the find the salary items of that salary detail ordered by prority 
           check each salary detail item
           if it is depend on attendance or production 
           then fetch the attendance or production
           if the attendance production uint does not match with 
           the salary iten unit then find the convertion rate from unit relation table
           then multiply to find the exact value  
           if pay head is computed value 
           then find the rule from the compoutation table
           parse rule and make meaningfull logic
           calculate the pay head amount           
           after calculating all pay head amount add them and find the net
        
        
           need 
        '''
        print('----hello world-----')
        attendences=Attendance.objects.filter(employee_id=employee_id).filter(date__gt='2018-12-09').filter(date__lte='2020-12-09')
        print(attendences)

        for attendence in attendences:
            print(attendence.production_attendance_type.name)
            print("{a} {b}".format(a=attendence.value,b=attendence.unit.name))
            print("--------------------------------------------")

        print('----hello world-----')




        return ""




