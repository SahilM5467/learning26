from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, "home.html")
def aboutUs(request):
    return render(request, "aboutUs.html")
def contactUs(request):
    return render(request, "contactUs.html")