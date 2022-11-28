from django.db import models

# Create your models here.

TASA_CHOICES = (
    ("TA", "TA"),
    ("SA", "SA"),
)

WORKING_PERMIT_STATUS_CHOICES = (
    ("Japanese", "Japanese"),
    ("International", "International"),
)

WORK_CATEGORY_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

MONTH_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)

class Student(models.Model):
    StudentID = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    TASA = models.CharField(max_length=2, choices=TASA_CHOICES, default="SA")
    WorkingPermitStatus = models.CharField(max_length=20, choices=WORKING_PERMIT_STATUS_CHOICES, default="Japanese")

class Lecturer(models.Model):
    Name =  models.CharField(max_length=100)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

class Course(models.Model):
    CourseID = models.CharField(max_length=10, unique=True)
    CourseName = models.CharField(max_length=100)

class Report(models.Model):
    Title = models.CharField(max_length=20)
    StudentID = models.ForeignKey(Student, to_field='StudentID', on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Course, to_field='CourseID', on_delete=models.DO_NOTHING)
    LecturerID = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING)
    Year = models.IntegerField()
    Month = models.IntegerField(choices=MONTH_CHOICES, default="1")
    TotalWorkingHours = models.DurationField()

class ReportHour(models.Model):
    ReportID = models.ForeignKey(Report, on_delete=models.CASCADE)
    Date = models.DateField()
    WorkCategory = models.IntegerField(choices=WORK_CATEGORY_CHOICES, default="1")
    Start = models.TimeField()
    End = models.TimeField()
    Break = models.DurationField()
    WorkingHours = models.DurationField()