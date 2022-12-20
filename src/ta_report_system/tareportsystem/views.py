from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def studentlogin(request):
    template = loader.get_template('tareportsystem/studentlogin.html')
    return HttpResponse(template.render())

def studentmain(request):
    template = loader.get_template('tareportsystem/studentmain.html')
    return HttpResponse(template.render())