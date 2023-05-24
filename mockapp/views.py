from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def firststr(request):
    return HttpResponse('first string http response')
def secondstr(request):
    return HttpResponse('second string http response')
def firsthtml(request):
    return render(request,'firsthtml.html')
def secondhtml(request):
    return render(request,'secondhtml.html')