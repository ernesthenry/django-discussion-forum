from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('This is the homepage')
    return render(request,'homepage.html')

def about(request):
    # return HttpResponse('We like Django')
    return render(request,'about.html')