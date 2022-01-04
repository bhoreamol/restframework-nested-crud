from .models import Department,Student
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['dept_id','dept_name','dept_head']

class StudentSerializer(serializers.ModelSerializer):
    # department=DepartmentSerializer(write_only=True)
    # full_name = serializers.SerializerMethodField()
    class Meta:
        model=Student
        fields=['std_id','first_name','last_name','department']

class StudentlistSerializer(serializers.ModelSerializer):
    department=DepartmentSerializer()
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['std_id', 'full_name', 'department']
    def get_full_name(self, obj):
        return obj.first_name + obj.last_name