from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from tareportsystem import models as tareportsystem_models
from django.contrib import messages
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar

# Create your views here.

def studentlogin(request):
    return render(request, 'tareportsystem/studentlogin.html')

def lecturerlogin(request):
    template = loader.get_template('tareportsystem/lecturerlogin.html')
    return render(request, 'tareportsystem/lecturerlogin.html')

def studentmain(request):
    uname = request.POST['Username']
    passw = request.POST['Password']
    if tareportsystem_models.Student.objects.filter(Username = uname, Password = passw).exists():
        template = loader.get_template('tareportsystem/studentmain.html')
        student = get_object_or_404(tareportsystem_models.Student, Username = uname)
        studentId = student.StudentID
        student_course_list = tareportsystem_models.Course.objects.filter(TASA__StudentID = studentId)
        context = {
            'student_course_list' : student_course_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        messages.error(request,'Username or password is not correct')
        return redirect('studentlogin')

def lecturermain(request):
    uname = request.POST['Username']
    passw = request.POST['Password']
    if tareportsystem_models.Lecturer.objects.filter(Username = uname, Password = passw).exists():
        template = loader.get_template('tareportsystem/lecturermain.html')
        lecturer = get_object_or_404(tareportsystem_models.Lecturer, Username = uname)
        lecturername = lecturer.Name
        lecturer_course_list = tareportsystem_models.Course.objects.filter(Lecturer__Name = lecturername)
        context = {
            'lecturer_course_list' : lecturer_course_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        messages.error(request,'Username or password is not correct')
        return redirect('lecturerlogin')

def studentcalendar(request):
    template = loader.get_template('tareportsystem/studentcalendar.html')
    return HttpResponse(template.render())

class CalendarView(generic.ListView):
    model = ReportHour
    template_name = 'tareportsystem/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()