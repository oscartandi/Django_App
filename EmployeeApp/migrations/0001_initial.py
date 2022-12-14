# Generated by Django 4.1.2 on 2022-11-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departments",
            fields=[
                ("DeparmtentId", models.AutoField(primary_key=True, serialize=False)),
                ("Departmentname", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Employees",
            fields=[
                ("EmployeeId", models.AutoField(primary_key=True, serialize=False)),
                ("EmployeeName", models.CharField(max_length=500)),
                ("Department", models.CharField(max_length=500)),
                ("DateOfJoining", models.DateField()),
                ("PhotoFileName", models.CharField(max_length=500)),
            ],
        ),
    ]
