from django.shortcuts import render, HttpResponse, redirect
from . models import Service
from . forms import ServiceForm


# Create your views here.

def serviceList(request):
    services = Service.objects.all().order_by("id").values()

    return render(request, "service/serviceList.html", {"services":services})

def createServiceForm(request):
    print(request.method)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save()
        return redirect("serviceList") 
    else :
        form = ServiceForm()
        return render(request, "service/createServiceForm.html",{"form":form})

def updateService(request,id):
    
    service = Service.objects.get(id=id) 
    
    if request.method == "POST":
        form = ServiceForm(request.POST,instance=service)
        form.save()
        return redirect("serviceList")
    else:
        form = ServiceForm(instance=service)    
        return render(request,"service/updateService.html",{"form":form})

def deleteService(request,id):
    print("id from url = ",id)
    Service.objects.filter(id=id).delete()
    return redirect("serviceList")