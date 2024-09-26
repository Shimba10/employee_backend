from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        name = self.request.query_params.get('name', None)
        department = self.request.query_params.get('department', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if department:
            queryset = queryset.filter(department__id=department)

        return queryset