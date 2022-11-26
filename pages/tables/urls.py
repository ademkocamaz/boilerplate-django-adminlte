from django.urls import path
from . import views

urlpatterns = [
    path('simple/', views.simple, name='tables_simple'),
    path('data/', views.data, name='tables_data'),
    path('jsgrid/', views.jsgrid, name='tables_jsgrid'),

]