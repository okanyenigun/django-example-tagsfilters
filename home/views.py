from django.shortcuts import render
from home.models import Car
from datetime import datetime   

def home_view(request):
    context = {"cars": Car.objects.all()}
    context["coordinates"] = [(1,2),(10,20),(100,200)]
    context["dicto"] = {"Germany": "Berlin","Turkey":"Ankara","France":"Paris"}
    context["empty_list"] = []
    context["numbers"] = [1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7]
    #return render(request, './templates/child.html', context)
    return render(request, './templates/index.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

def cycle_view(request):
    items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
    return render(request, 'cycle.html', {'items': items})

def product_list(request):
    cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]
    context = {'country_list': cities}
    return render(request, 'product.html', context)

def tag_view(request):
    context={"date":datetime.now(), "value":5} 

    return render(request, './templates/tags.html', context)