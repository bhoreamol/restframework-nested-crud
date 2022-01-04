
from django.db import models
class Department(models.Model):
    dept_id=models.IntegerField()
    dept_name=models.CharField(max_length=50)
    dept_head=models.CharField(max_length=70)

class Student(models.Model):
    std_id=models.IntegerField()
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='dept')

# Create your models here.
