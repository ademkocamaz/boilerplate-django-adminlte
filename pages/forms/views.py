from django.shortcuts import render

# Create your views here.

def general(request):
    return render(request, 'pages/forms/general.html')

def advanced(request):
    return render(request, 'pages/forms/advanced.html')

def editors(request):
    return render(request, 'pages/forms/editors.html')

def validation(request):
    return render(request, 'pages/forms/validation.html')