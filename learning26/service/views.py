from django.shortcuts import render, HttpResponse, redirect
from . models import Service
from . forms import ServiceForm
from django.contrib import messages


# Create your views here.

def serviceList(request):
    services = Service.objects.all()
    return render(request,"service/serviceList.html",{"services":services})

def createServiceForm(request):

    if request.method == "POST":
        form = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Service created successfully!")
            return redirect("serviceList")
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = ServiceForm()

    return render(request, "service/createServiceForm.html", {"form": form})