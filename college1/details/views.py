from django.shortcuts import render
from .serializers import DepartmentSerializer,StudentSerializer, StudentlistSerializer
from rest_framework import viewsets
from .models import Department,Student
# from rest_framework.filters import SearchFilter

# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return StudentlistSerializer
        else:
            return StudentSerializer
    # filter_backends = [SearchFilter]
    # search_fields=['std_id']
# Create your views here.
