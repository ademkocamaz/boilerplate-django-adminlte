from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, 'home/index.html')

def index(request):
    return render(request, 'home/index.html')

def index2(request):
    return render(request, 'home/index2.html')

def index3(request):
    return render(request, 'home/index3.html')

def iframe(request):
    return render(request, 'home/iframe.html')

def iframe_dark(request):
    return render(request, 'home/iframe-dark.html')
