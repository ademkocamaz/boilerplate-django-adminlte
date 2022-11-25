from django.urls import path
from . import views

urlpatterns = [
    path('chartjs', views.chartjs, name='chartjs'),
    path('flot', views.flot, name='flot'),
    path('inline', views.inline, name='inline'),
    path('uplot', views.uplot, name='uplot'),
]