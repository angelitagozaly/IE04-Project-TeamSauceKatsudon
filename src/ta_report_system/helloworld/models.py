from django.db import models

# Create your models here.

class Lecturer(models.Model):
    name = models.CharField()

class Student(models.Model):
    name = models.CharField()

class Report(models.Model):
    course_name = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, on_delete= models.SET_NULL)
