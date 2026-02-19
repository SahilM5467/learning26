from django.shortcuts import render, HttpResponse, redirect
from . models import Service
from . forms import ServiceForm


# Create your views here.

def serviceList(request):
    services = Service.objects.all()
    return render(request,"service/serviceList.html",{"services":services})

def createServiceForm(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"service/createServiceForm.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"service/createServiceForm.html",{"form":form})