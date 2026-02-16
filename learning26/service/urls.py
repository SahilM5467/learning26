from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('serviceList', views.serviceList, name="serviceList"),
    path('createServiceForm', views.createServiceForm, name="createServiceForm"),
    path("updateService/<int:id>",views.updateService,name="updateService"),
    path("deleteService/<int:id>",views.deleteService,name="deleteService"),
]







