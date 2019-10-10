from django.shortcuts import render
from django.http import HttpResponse
import datetime
from test_app.models import Four


# Create your views here.
def hi(req):
    return HttpResponse('<h1>welcome</h1>')

def date_t(req):
    time=datetime.datetime.now()
    n='sam'
    a=23
    s={'t':time,'nn':n,'aa':a}
    return render(req,'result.html',context=s)

def o(req):
    return render(req,'one.html')

def n(req):
    four=Four.objects.all()
    return render(req,'one.html',{'four':four})    