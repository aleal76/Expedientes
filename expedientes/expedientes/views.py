from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello dde homepage")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("Hello from about page")
    return render(request, 'about.html')