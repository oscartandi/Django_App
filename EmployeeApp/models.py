from django.db import models

# Create your models here.


class Departments(models.Model):
    DeparmtentId=models.AutoField(primary_key=True)
    Departmentname=models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
