from django.urls import path, include
from . import views

urlpatterns = [
    path('widgets/', views.widgets, name='widgets'),
    path('layout/', include('pages.layout.urls')),
    path('charts/', include('pages.charts.urls')),

]
