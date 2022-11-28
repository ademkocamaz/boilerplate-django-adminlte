from django.urls import path
from . import views

urlpatterns = [
    path('simple/', views.simple, name='search_simple'),
    path('simple-results/', views.simple_results, name='search_simple-results'),
    path('enhanced/', views.enhanced, name='search_enhanced'),
    path('enhanced-results/', views.enhanced_results, name='search_enhanced-results'),
]