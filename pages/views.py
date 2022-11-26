from django.shortcuts import render

# Create your views here.


def widgets(request):
    return render(request, 'pages/widgets.html')

def calendar(request):
    return render(request, 'pages/calendar.html')
