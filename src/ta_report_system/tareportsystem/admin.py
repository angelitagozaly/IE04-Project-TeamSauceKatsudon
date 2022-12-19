from django.contrib import admin
from django import forms

# Register your models here.

from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('StudentID', 'Name', 'TASA')
admin.site.register(Student, StudentAdmin)

from .models import Lecturer
admin.site.register(Lecturer)

from .models import Course
class CourseAdmin(admin.ModelAdmin):
    list_display = ('CourseID', 'CourseName')
admin.site.register(Course, CourseAdmin)

from .models import Report
class ReportAdmin(admin.ModelAdmin):
    list_display = ('Title', 'StudentID', 'CourseID', 'Year', 'Month')
    list_filter = ('CourseID', 'Year', 'Month')
admin.site.register(Report, ReportAdmin)

from .models import ReportHour
class ReportHourAdmin(admin.ModelAdmin):
    list_display = ('ReportTitle', 'Date')
admin.site.register(ReportHour, ReportHourAdmin)

# Change time format
#class timeFormat(forms.Form):
#    from_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
#admin.site.register(timeFormat)