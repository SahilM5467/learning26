from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, "home.html")
def aboutUs(request):
    return render(request, "aboutUs.html")
def contactUs(request):
    return render(request, "contactUs.html")
def recipe(request):
    ingredient = ["Masala","Tomato","Onion","Salt"]
    data = { "name":"Maggie","time":5, "ingredient":ingredient }
    return render(request, "recipe.html",data)
def team(request):
    players = ["Shubhman Gill","Sai Sudarshan","Jos Buttler","Mohammad Siraj","Rashid Khan","Sai Kishore","Prasidh Krishna"]
    data = {"name":"Gujarat Titans", "captain":"Shubhman Gill","players":players,"trophies":1, "owner":"Torrent Group"}
    return render(request,"team.html",data)