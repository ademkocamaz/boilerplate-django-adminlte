from django.shortcuts import render

# Create your views here.


def widgets(request):
    return render(request, 'pages/widgets.html')

def calendar(request):
    return render(request, 'pages/calendar.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def kanban(request):
    return render(request, 'pages/kanban.html')
