from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("HELLO WORLD")
def mydate(request,year,month,day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))
