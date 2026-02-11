from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('employeeList', views.employeeList),
    path('employeeFilter', views.employeeFilter),
    path('createEmployeeForm', views.createEmployeeForm),
    path('createCourseForm', views.createCourseForm),
    path('createCarForm', views.createCarForm),
    path('createBikeForm', views.createBikeForm),
]







