from django.shortcuts import render

# Create your views here.
def top_nav(request):
    return render(request,'pages/layout/top-nav.html')