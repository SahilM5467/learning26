from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('employeeList', views.employeeList, name="employeeList"),
    path('employeeFilter', views.employeeFilter),
    path('createEmployeeForm', views.createEmployeeForm, name="createEmployeeForm"),

    path('createCourseForm', views.createCourseForm),
    path('createCarForm', views.createCarForm),
    path('createBikeForm', views.createBikeForm),

    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
    path("updateemployee/<int:id>",views.updateEmployee,name="updateEmployee"),
    path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
    path("sortEmployee/<int:id>",views.sortEmployee,name="sortEmployee"),
]







