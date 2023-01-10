from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from tareportsystem import models as tareportsystem_models
from django.contrib import messages

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
        return HttpResponse(template.render())
    else:
        messages.error(request,'Username or password is not correct')
        return redirect('studentlogin')

def lecturermain(request):
    uname = request.POST['Username']
    passw = request.POST['Password']
    if tareportsystem_models.Lecturer.objects.filter(Username = uname, Password = passw).exists():
        template = loader.get_template('tareportsystem/lecturermain.html')
        return HttpResponse(template.render())
    else:
        messages.error(request,'Username or password is not correct')
        return redirect('lecturerlogin')

def studentcalendar(request):
    template = loader.get_template('tareportsystem/studentcalendar.html')
    return HttpResponse(template.render())