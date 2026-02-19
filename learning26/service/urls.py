from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("serviceList/",views.serviceList,name="serviceList"),
    path("createServiceForm/",views.createServiceForm,name="createServiceForm"),
]







