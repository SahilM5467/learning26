from django.shortcuts import render
from . models import Employee
from django.db.models import Q


# Create your views here.
def employeeList(request):
    employees1 = Employee.objects.all().values()
    employees2 = Employee.objects.all().values_list()
    print(employees1)
    print(employees2)

    return render(request, "employee/employeeList.html", {'employees1':employees1,'employees2':employees2})

def employeeFilter(request):
    
    q1 = Employee.objects.filter(name="Sahil").values()
    print("Query 1 : ",q1)

    q2 = Employee.objects.filter(post="Developer").values()
    print("Query 2 : ",q2)

    q3 = Employee.objects.filter(name="Sahil",post="Developer").values()
    print("Query 3 : ",q3)

    q4 = Employee.objects.filter(Q(name="Hardik") | Q(post="Developer")).values()
    print("Query 4 : ",q4)

    q5 = Employee.objects.filter(age__gt=21).values()
    print("Query 5 : ",q5)
    q6 = Employee.objects.filter(age__gte=21).values()
    print("Query 6 : ",q6)

    q7 = Employee.objects.filter(age__lt=21).values()
    print("Query 7 : ",q7)
    q8 = Employee.objects.filter(age__lte=21).values()
    print("Query 8 : ",q8)

    q9 = Employee.objects.filter(post__exact="Developer").values()
    print("Query 9 : ",q9)

    q10 = Employee.objects.filter(post__exact="developer").values()
    print("Query 10 : ",q10)
    q11 = Employee.objects.filter(post__iexact="developer").values()
    print("Query 11 : ",q11)

    q12 = Employee.objects.filter(name__contains="S").values()
    print("Query 12 : ",q12)
    q13 = Employee.objects.filter(name__icontains="s").values()
    print("Query 13 : ",q13)

    q14 = Employee.objects.filter(name__startswith="S").values()
    print("Query 14 : ",q14)
    q15 = Employee.objects.filter(name__istartswith="s").values()
    print("Query 15 : ",q15)

    q16 = Employee.objects.filter(name__endswith="k").values()
    print("Query 16 : ",q16)
    q17 = Employee.objects.filter(name__iendswith="K").values()
    print("Query 17 : ",q17)

    q18 = Employee.objects.filter(name__in=["Sahil","Jay"]).values()
    print("Query 18 : ",q18)

    q19 = Employee.objects.filter(salary__range=[15000,25000]).values()
    print("Query 19 : ",q19)

    q20 = Employee.objects.order_by("age").values()
    print("Query 20 : ",q20)
    q21 = Employee.objects.order_by("-age").values()
    print("Query 21 : ",q21)

    q22 = Employee.objects.order_by("salary").values()
    print("Query 22 : ",q22)
    q23 = Employee.objects.order_by("-salary").values()
    print("Query 23 : ",q23)

    q24 = Employee.objects.order_by("post","-id").values()
    print("Query 24 : ",q24)

    
    return render(request, "employee/employeeFilter.html")






