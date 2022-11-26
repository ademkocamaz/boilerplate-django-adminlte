from django.shortcuts import render

# Create your views here.

def simple(request):
    return render(request, 'pages/tables/simple.html')

def data(request):
    return render(request, 'pages/tables/data.html')

def jsgrid(request):
    return render(request, 'pages/tables/jsgrid.html')