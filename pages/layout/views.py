from django.shortcuts import render

# Create your views here.
def top_nav(request):
    return render(request,'pages/layout/top-nav.html')

def top_nav_sidebar(request):
    return render(request,'pages/layout/top-nav-sidebar.html')

def boxed(request):
    return render(request, 'pages/layout/boxed.html')

def fixed_sidebar(request):
    return render(request, 'pages/layout/fixed-sidebar.html')

def fixed_sidebar_custom(request):
    return render(request, 'pages/layout/fixed-sidebar-custom.html')

def fixed_topnav(request):
    return render(request, 'pages/layout/fixed-topnav.html')

def fixed_footer(request):
    return render(request, 'pages/layout/fixed-footer.html')

def collapsed_sidebar(request):
    return render(request, 'pages/layout/collapsed-sidebar.html')