from django.shortcuts import render

# Create your views here.
def studentHome(request):
    return render(request, "studentFile/studentHome.html")

def studentDetails(request):
    data = {"name":"Sahil", "college":"SCE","department":"IT"}
    return render(request, "studentFile/studentDetails.html", data)

def studentMarks(request):
    marks = {"Sahil":95, "Devansh":80, "Mitul":75 }
    return render(request, "studentFile/studentMarks.html", marks)