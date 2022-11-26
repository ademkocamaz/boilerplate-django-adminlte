from django.urls import path
from . import views

urlpatterns = [
    path('chartjs/', views.chartjs, name='charts_chartjs'),
    path('flot/', views.flot, name='charts_flot'),
    path('inline/', views.inline, name='charts_inline'),
    path('uplot/', views.uplot, name='charts_uplot'),
]