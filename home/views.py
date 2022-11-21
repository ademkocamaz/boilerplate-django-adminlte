from django.shortcuts import render

# Create your views here.


def starter(request):
    return render(request, 'home/starter.html')


def index(request):
    return render(request, 'home/index.html')


def index2(request):
    return render(request, 'home/index2.html')


def index3(request):
    return render(request, 'home/index3.html')
