from django.urls import path
from . import views

urlpatterns = [
    path('student-login', views.studentlogin, name='studentlogin'),
    path('student-main', views.studentmain, name='studentmain'),
]