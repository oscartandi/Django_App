from rest_framework import serializers
from EmployeeApp.models import Departments, Employees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fileds=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        field=('EmployeeId','EmployeeName', 'Deparment', 'DateofJoining','PhotoFileName')

