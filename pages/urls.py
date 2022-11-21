from django.urls import path
from . import views

urlpatterns = [
    path('widgets', views.widgets, name='widgets'),

]
