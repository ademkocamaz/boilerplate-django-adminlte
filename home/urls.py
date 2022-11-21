from django.urls import path
from . import views

urlpatterns = [
    path('', views.starter, name='starter'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
]
