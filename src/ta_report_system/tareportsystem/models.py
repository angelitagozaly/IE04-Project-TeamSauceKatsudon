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
    StudentID = models.CharField("Student ID", max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    TASA = models.CharField(max_length=2, choices=TASA_CHOICES, default="SA")
    WorkingPermitStatus = models.CharField("Working Permit Status", max_length=20, choices=WORKING_PERMIT_STATUS_CHOICES, default="Japanese")

    def __str__(self):
        return self.StudentID

class Lecturer(models.Model):
    Name =  models.CharField(max_length=100)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Course(models.Model):
    CourseID = models.CharField("Course ID", max_length=10, unique=True)
    CourseName = models.CharField("Course Name", max_length=100)
    TASA = models.ManyToManyField(Student)
    Lecturer = models.ManyToManyField(Lecturer)

    def __str__(self):
        return self.CourseName

class Report(models.Model):
    Title = models.CharField(max_length=100)
    StudentID = models.ForeignKey(Student, to_field='StudentID', on_delete=models.CASCADE, verbose_name="Student ID")
    CourseID = models.ForeignKey(Course, to_field='CourseID', on_delete=models.DO_NOTHING, verbose_name="Course ID")
    LecturerID = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING)
    Year = models.IntegerField()
    Month = models.CharField(max_length=3, choices=MONTH_CHOICES, default="1")
    TotalWorkingHours = models.DurationField("Total Working Hours")

    def __str__(self):
        return str(self.Title)

class ReportHour(models.Model):
    ReportTitle = models.ForeignKey(Report, on_delete=models.CASCADE, verbose_name="Report Title")
    Date = models.DateField()
    WorkCategory = models.CharField("Work Category", max_length=5, choices=WORK_CATEGORY_CHOICES, default="1")
    Start = models.TimeField()
    End = models.TimeField()
    Break = models.DurationField()
    WorkingHours = models.DurationField("Working Hours")

    def __str__(self):
        return str(self.ReportTitle)