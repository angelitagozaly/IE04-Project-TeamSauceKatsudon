from django.contrib import admin

# Register your models here.

from .models import Student
admin.site.register(Student)

from .models import Lecturer
admin.site.register(Lecturer)

from .models import Course
admin.site.register(Course)

from .models import Report
admin.site.register(Report)

from .models import ReportHour
admin.site.register(ReportHour)
