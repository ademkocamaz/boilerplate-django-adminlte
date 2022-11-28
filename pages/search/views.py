from django.shortcuts import render

# Create your views here.

def simple(request):
    return render(request, 'pages/search/simple.html')

def simple_results(request):
    return render(request, 'pages/search/simple-results.html')

def enhanced(request):
    return render(request, 'pages/search/enhanced.html')

def enhanced_results(request):
    return render(request, 'pages/search/enhanced-results.html')