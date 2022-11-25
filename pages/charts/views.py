from django.shortcuts import render

# Create your views here.

def chartjs(request):
    return render(request, 'pages/charts/chartjs.html')

def flot(request):
    return render(request, 'pages/charts/flot.html')

def inline(request):
    return render(request, 'pages/charts/inline.html')

def uplot(request):
    return render(request, 'pages/charts/uplot.html')