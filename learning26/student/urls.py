from django.urls import path
from . import views

urlpatterns = [
   path("home/",views.studentHome),
   path("details/",views.studentDetails),
   path("marks/",views.studentMarks),
  
]