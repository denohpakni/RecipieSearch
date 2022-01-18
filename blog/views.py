from django.shortcuts import render
from django.http import HttpResponse

import requests
from requests.api import post  #this belongs to python and not django

'''Application ID
6244a255
Application Keys
f7613762b9c884d1ca2d69a1efc3075a
'''
# Create your views here.

def home(request):
    query = "lamb" # you can change this to whatever you want to search a recipe
    response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+query+"&app_id=6244a255&app_key=f7613762b9c884d1ca2d69a1efc3075a")
    jsonResponse = response.json()
    recipes = jsonResponse['hits']
    return render(request,'home.html', {'recipes':recipes})

def search(request):
    if request.method =="POST":
        userText = request.POST.get('userText')
        response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+userText+"&app_id=6244a255&app_key=f7613762b9c884d1ca2d69a1efc3075a")
        jsonResponse = response.json()
        recipes = jsonResponse['hits']
        return render(request,'home.html', {'recipes':recipes})
    else:
        return render(request,"gome.html")
