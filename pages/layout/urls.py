from django.urls import path
from . import views

urlpatterns = [
    path('top-nav/', views.top_nav, name='top-nav')
]
