from django.urls import path
from . import views

urlpatterns = [
    path('student-login', views.studentlogin, name='studentlogin'),
    path('lecturer-login', views.lecturerlogin, name='lecturerlogin'),
    path('student-main', views.studentmain, name='studentmain'),
    path('lecturer-main', views.lecturermain, name='lecturermain'),
    path('student-calendar', views.studentcalendar, name='calendar'),
    path('calendar', views.CalendarView.as_view(), name='calendartest'),
]