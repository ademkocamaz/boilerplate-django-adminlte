from django.shortcuts import render

# Create your views here.


def general(request):
    return render(request, 'pages/ui/general.html')

def icons(request):
    return render(request, 'pages/ui/icons.html')

def buttons(request):
    return render(request, 'pages/ui/buttons.html')

def sliders(request):
    return render(request, 'pages/ui/sliders.html')

def modals(request):
    return render(request, 'pages/ui/modals.html')

def navbar(request):
    return render(request, 'pages/ui/navbar.html')

def timeline(request):
    return render(request, 'pages/ui/timeline.html')

def ribbons(request):
    return render(request, 'pages/ui/ribbons.html')
